import requests
from twilio.rest import Client

API_KEY = "ec4a0970326681c5a3cadad161207745"
URL = "https://api.openweathermap.org/data/2.5/weather"

SID = "AC3db9f3a108412b6dba78702733863781"
token = "db97ede9212432f40cac7d8ab0be25af"
phone_number = "+17756289693"

response = requests.get(URL+f"?q=Gerponville, fr&APPID={API_KEY}")
response.raise_for_status()
lon, lat = response.json()["coord"]["lon"], response.json()["coord"]["lat"]

three_hours_api = f"""https://api.openweathermap.org/data/2.5/forecast?lat={
    lat}&lon={lon}&appid={API_KEY}&cnt=4"""
resultat = requests.get(three_hours_api).json()
for i in resultat["list"]:
    if i["weather"][0]["id"] >= 700:
        print("test")

client = Client(SID, token)

msg = client.messages.create(
    body="test",
    to=phone_number,
    from_="+33681954028"
)
