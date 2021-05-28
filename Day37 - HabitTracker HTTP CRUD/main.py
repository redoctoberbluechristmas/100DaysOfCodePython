import os
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from datetime import datetime

keyvault_url = os.environ.get('KEYVAULT_URL')
credential = DefaultAzureCredential()
client = SecretClient(keyvault_url, credential)

TOKEN = client.get_secret('pixela-token').value

graph_id = "graph1"
graph_name = "readinggraph"
graph_unit = "pages"
graph_type = "int"
graph_color = "ajisaid"

PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')
PIXELA_BASE_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_BASE_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_PIXEL_POST_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{graph_id}"
#PIXELA_PIXEL_PUT_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{graph_id}/{datetime.today().strftime('%Y%m%d')}"

user_parameters = {
    "token": TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Post request to create user account
#response = requests.post(url=PIXELA_BASE_ENDPOINT, json=user_parameters)

http_headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_post_parameters = {
    "username": PIXELA_USERNAME,
    "id": graph_id,
    "name": graph_name,
    "unit": graph_unit,
    "type": graph_type,
    "color": graph_color,
}

# Post request to create graph
# graph_response = requests.post(url=PIXELA_GRAPH_CREATION_ENDPOINT, headers=http_headers, json=graph_post_parameters)
# print(graph_response.text)
# print(graph_response.status_code)

pages_read_today = input("How many pages did you read today? ")

#Post a pixel to an existing graph
pixel_post_parameters = {
    "date": datetime.today().strftime('%Y%m%d'),
    "quantity": pages_read_today,
}

pixel_post_response = requests.post(url=PIXELA_PIXEL_POST_ENDPOINT, headers=http_headers, json=pixel_post_parameters)
# print(pixel_post_response.text)
# print(pixel_post_response.status_code)

# Update an existing pixel

# pixel_put_parameters = {
#     "quantity": "20",
# }

# put_year = "2021"
# put_month = "05"
# put_day = "27"
# PIXELA_PIXEL_PUT_DELETE_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{graph_id}/{put_year}{put_month}{put_day}"

# pixel_put_response = requests.put(url=PIXELA_PIXEL_PUT_DELETE_ENDPOINT, headers=http_headers, json=pixel_put_parameters)
# print(pixel_put_response.text)
# print(pixel_put_response.status_code)

# pixel_delete_response = requests.delete(url=PIXELA_PIXEL_PUT_DELETE_ENDPOINT, headers=http_headers)
# print(pixel_delete_response.text)
# print(pixel_delete_response.status_code)