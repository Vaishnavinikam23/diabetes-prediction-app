import requests

url = "https://diabetes-prediction-model-2ykw.onrender.com/predict"
headers = {
    "User-Agent": "Mozilla/5.0",  # Mimic a browser
    "Content-Type": "application/json"  # Ensure JSON format
}
data = {"features": [1, 100, 80, 20, 30, 25.0, 0.5, 30]}

response = requests.post(url, json=data, headers=headers)

print("Response Status Code:", response.status_code)
print("Response Text:", response.text)  # Debugging
try:
    print("Parsed JSON:", response.json())  
except requests.exceptions.JSONDecodeError:
    print("⚠️ Error: API response is not JSON formatted!")
