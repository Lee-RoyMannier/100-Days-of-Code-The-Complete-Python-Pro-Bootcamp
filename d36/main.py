import requests
import datetime
import os
import smtplib

MY_EMAIL = "XXXX"
PASSWORD = "XXXXX"

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = os.environ.get("API_ALPHA")
param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=param)
data = response.json()
close_value = [float(value["4. close"])
               for (key, value) in data["Time Series (Daily)"].items()]
yesterday_value = close_value[1]
day_before_yesterday = close_value[2]

diff_abs = abs(day_before_yesterday - yesterday_value)
perc_diff = (diff_abs/yesterday_value)*100
params = {
    "apiKey": os.environ.get("NEW_API"),
    "q": COMPANY_NAME,
}
connection = requests.get(NEWS_ENDPOINT, params=params)
data_new = connection.json()
articles = data_new["articles"][0:3]
informations = [(article["title"], article["description"])
                for article in articles]
start = "🔻" if perc_diff >= 5 else "🔺"

for i in range(0, 3):
    msg = f"""SUBJECT:{STOCK_NAME}: {start}{int(perc_diff)}% \n\n
            Headlines: {informations[i][0]}\n
            Brief: {informations[i][1]}"""
    with smtplib.SMTP_SSL("smtp.gmail.com") as mail:
        mail.login(user=MY_EMAIL, password=PASSWORD)
        mail.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="leeroymannier@hotmail.fr",
            msg=msg.encode('utf-8'),

        )
