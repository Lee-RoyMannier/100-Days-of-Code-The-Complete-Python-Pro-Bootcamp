import requests

params = {
    "amount": 10,
    "type": "boolean",
}
URL = "https://opentdb.com/api.php"
response = requests.get(url=URL, params=params)
response.raise_for_status()

question_data = response.json()["results"]
