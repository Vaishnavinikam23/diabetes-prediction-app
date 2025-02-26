from flask import Flask, request, jsonify
import pickle  # Import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

@app.route("/", methods=["GET"])
def home():
    return "Flask backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  
    features = np.array(data["features"]).reshape(1, -1)
    
    # Normalize features using the same scaler used during training
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

