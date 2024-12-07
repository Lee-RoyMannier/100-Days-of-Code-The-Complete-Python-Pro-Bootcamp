import requests
from datetime import datetime
import smtplib

from config import MY_EMAIL, PASSWORD

MY_LAT = 49.751294
MY_LONG = 0.565546

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
close_to_me = (
    MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if close_to_me and (time_now.hour >= sunset or time_now.hour <= sunrise):
    with smtplib.SMTP_SSL("smtplib.gmail.com") as mail:
        mail.login(password=PASSWORD, user=MY_EMAIL)
        mail.sendmail(
            to_addrs="test@test.fr",
            from_addr=MY_EMAIL,
            msg="Subject:LOOK UP \n\n check the ISS in the sky!!"
        )
