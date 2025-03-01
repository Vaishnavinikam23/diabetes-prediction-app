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
diabetes_pedigree_function = st.sidebar.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.sidebar.number_input("Age", min_value=10, max_value=100, value=30)

def predict_diabetes(features):
    url = "https://diabetes-prediction-app-u88a.onrender.com/predict"  # Correct API URL
    payload = {"features": features}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an error for bad status codes

        data = response.json()
        return data.get("prediction", "Error: No prediction key in response")

    except requests.exceptions.RequestException as e:
        return f"Error: API request failed ({e})"

if st.sidebar.button("🔍 Predict Diabetes"):
    result = predict_diabetes([
        pregnancies, glucose, blood_pressure, skin_thickness, insulin,
        bmi, diabetes_pedigree_function, age
    ])

    st.subheader("🩺 **Prediction Result**")
    if result == 1:
        st.error("⚠️ **Diabetic - Please consult a doctor immediately.**")
    elif result == 0:
        st.success("✅ **Non-Diabetic - Your health is in good condition.**")
    else:
        st.warning(f"❌ **API Error: {result}**")
