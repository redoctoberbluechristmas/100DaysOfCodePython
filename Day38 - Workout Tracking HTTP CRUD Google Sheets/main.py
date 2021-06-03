import os
import requests
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from datetime import datetime

KEYVAULT_URL = os.environ.get('KEYVAULT_URL')
CREDENTIAL = DefaultAzureCredential()
client = SecretClient(KEYVAULT_URL, CREDENTIAL)


AGE = 21
WEIGHT = 70
HEIGHT = 178
GENDER = "male"

NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = client.get_secret('sheety-endpoint').value

APP_ID = client.get_secret('nutritionix-app-id').value
API_KEY = client.get_secret('nutritionix-api-key').value

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutritionix_params = {
    "query": input("What exercises did you do? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_EXERCISE_ENDPOINT, headers=nutritionix_headers, json=nutritionix_params)
exercise_data = response.json()['exercises']
print(exercise_data)

today_date = datetime.today().strftime('%d/%m/%Y')
current_time = datetime.today().strftime('%H:%M:%S')


for exercise in exercise_data:
    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_headers = {
        "Authorization": f"Bearer {client.get_secret('sheety-token').value}",
    }


    sheety_post_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=sheety_headers)
    print(sheety_post_response.status_code)
    print(sheety_post_response.text)