import requests
import datetime

username = "leeroymannier"
token = "xxxx"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {

    "token": token,

    "username": username,

    "agreeTermsOfService": "yes",

    "notMinor": "yes"

}

# Create the user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

# Create the Graph
# config = {
#     "id": "graph1",
#     "name": "cycle text",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji",
# }

headers = {
    "X-USER-TOKEN": token
}

# graph = f"{pixela_endpoint}/{username}/graphs"
# response = requests.post(url=graph, json=config, headers=headers)
# print(response.text)

# Update the Graph
graph_url = f"{pixela_endpoint}/{username}/graphs/graph1"
today = datetime.datetime.now().strftime(format="%Y%m%d")
params_graph = {
    "name": "graph1",
    "unit": "Km",
    "color": "ichou",
    "date":  today,
    "quantity": "15"
}

response = requests.put(url=graph_url, json=params_graph, headers=headers)
print(response.text)
