import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="Diabetes Prediction AI", layout="wide")

st.markdown("<h1 style='text-align: center; color: #154360;'>🔬 Diabetes Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🏥 A machine learning-based tool for early diabetes detection</h3><hr>", unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.title("🩺 Patient Details")
pregnancies = st.sidebar.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.sidebar.number_input("Glucose Level", min_value=50, max_value=200, value=100)
blood_pressure = st.sidebar.number_input("Blood Pressure", min_value=40, max_value=130, value=80)
skin_thickness = st.sidebar.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.sidebar.number_input("Insulin Level", min_value=0, max_value=900, value=30)
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=30)

def predict_diabetes(features):
    url = "http://127.0.0.1:10000/predict"  # Local Flask URL
    payload = {"features": features}
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json().get("prediction", "Error: No prediction key in response")
    else:
        return f"Error: API not responding, Status Code: {response.status_code}"

if st.sidebar.button("🔍 Predict Diabetes"):
    result = predict_diabetes([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age])

    st.subheader("🩺 **Prediction Result**")
    if result == 1:
        st.error("⚠️ **Diabetic - Please consult a doctor immediately.**")
    elif result == 0:
        st.success("✅ **Non-Diabetic - Your health is in good condition.**")
    else:
        st.warning("❌ **API Error: Unable to get prediction.**")
