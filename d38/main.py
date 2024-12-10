import requests
import datetime

URL = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"
API_KEY = "xxx"
API_ID = "xxx"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

params = {
    "query": input("exercice ?").title(),
    "weight_kg": 90,
    "height_cm": 185,
    "age": 30,
}

response = requests.post(
    url=f"{URL}/{END_POINT}", json=params, headers=headers)
data = response.json()

# Sheety API
PROJECT_NAME = "workout"
SHEET_NAME = "workouts"
EMAIL = "xxx"
PWD = "xxx"
auth = (EMAIL, PWD)
URL = f"https://api.sheety.co/5d62447c7c1c96db7460bb113a7be918/{
    PROJECT_NAME}/{SHEET_NAME}"
sheet_header = {
    "Authorization": "Basic bG1hbm5pZXI6dGVzdDEyMw==",
    "Content-Type": "application/json",
}
print(data)
for exercice in data["exercises"]:
    resume = {
        "workout": {
            "date": datetime.datetime.now().strftime("%Y/%m/%d"),
            "time": datetime.datetime.now().strftime("%X"),
            "exercise": exercice["name"],
            "duration": exercice["duration_min"],
            "calories": exercice["nf_calories"]
        }}
    test = requests.post(url=URL, json=resume, headers=sheet_header, auth=auth)
