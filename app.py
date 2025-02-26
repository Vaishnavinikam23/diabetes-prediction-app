import pickle
import numpy as np
import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="Diabetes Prediction AI", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: #2C3E50;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            color: #7F8C8D;
            font-size: 18px;
        }
        .stButton > button {
            background-color: #D6EAF8;
            color: #2C3E50;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #AED6F1;
        }
        .prediction-box {
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .diabetic {
            background-color: #FF5252;
            color: white;
        }
        .non-diabetic {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Page Header
st.markdown("<h1 class='main-title'>🔬 Diabetes Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>🏥 A machine learning-based tool for early diabetes detection</h3><hr>", unsafe_allow_html=True)

# Sidebar Input Fields
st.sidebar.title("🩺 Patient Details")
pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.sidebar.number_input("Glucose Level", min_value=50, max_value=200, value=100)
blood_pressure = st.sidebar.number_input("Blood Pressure", min_value=40, max_value=130, value=80)
skin_thickness = st.sidebar.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.sidebar.number_input("Insulin Level", min_value=0, max_value=900, value=30)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=30)

# Function to send API request to Flask
def predict_diabetes(features):
    url = "http://127.0.0.1:5000/predict"  # Flask API URL
    payload = {"features": features}  # JSON format
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()["prediction"]  # API se prediction result
    else:
        return "Error: API not responding"

# Prediction Button
if st.sidebar.button("🔍 Predict Diabetes"):
    result = predict_diabetes([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age])

    st.subheader("🩺 **Prediction Result**")
    if result == 1:
        st.markdown('<div class="prediction-box diabetic">⚠️ Diabetic - Please consult a doctor immediately.</div>', unsafe_allow_html=True)
    elif result == 0:
        st.markdown('<div class="prediction-box non-diabetic">✅ Non-Diabetic - Your health is in good condition.</div>', unsafe_allow_html=True)
    else:
        st.error("❌ API Error: Unable to get prediction. Check if Flask is running.")
