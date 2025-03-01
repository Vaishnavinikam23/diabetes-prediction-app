import os
from flask import Flask, request, jsonify
from flask_cors import CORS  
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  

# Load Model & Scaler
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

@app.route("/", methods=["GET"])
def home():
    return "Flask backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  
    features = np.array(data["features"]).reshape(1, -1)
    features_scaled = scaler.transform(features)  
    prediction = model.predict(features_scaled)
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render assigns PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)
