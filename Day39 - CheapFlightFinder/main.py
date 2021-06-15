import os
from datetime import datetime, timedelta
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

key_vault_url = os.environ.get('KEYVAULT_URL')
credential = DefaultAzureCredential()
client = SecretClient(key_vault_url, credential)

SHEETY_ENDPOINT = client.get_secret('sheety-endpoint').value
SHEETY_TOKEN = client.get_secret('sheety-token').value

KIWI_API_KEY = client.get_secret('kiwi-api-key').value
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"

SMS_ACCOUNT_SID = client.get_secret('sms-account-sid').value
SMS_AUTH_TOKEN = client.get_secret('sms-auth-token').value
SOURCE_PHONE_NUMBER = client.get_secret('source-phone-number').value
DEST_PHONE_NUMBER = client.get_secret('dest-phone-number').value



HOME_CITY_IATA_CODE = "SEA"
tomorrow_date = (datetime.today() + timedelta(days=1)).strftime('%d/%m/%Y')
to_date = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')


def update_iata_column(sheet_data):
    for i in sheet_data:
        if i['iataCode'] == "":
            object_endpoint = SHEETY_ENDPOINT + '/' + str(i['id'])
            city = i['city']
            iata_post_parameters = {
                "price": {
                    "iataCode": flight_searcher.get_iata_code(city)
                }
            }
            data_manager.edit_iata_data(object_endpoint, iata_post_parameters)


def search_for_flights(sheet_data):
    tomorrow_date = (datetime.today() + timedelta(days=1)).strftime('%d/%m/%Y')
    to_date = (datetime.today() + timedelta(days=180)).strftime('%d/%m/%Y')
    # Search for Flights for all "City" entries in sheety spreadsheet.
    for i in sheet_data:
        flight = flight_searcher.find_flights(HOME_CITY_IATA_CODE, i['iataCode'], tomorrow_date, to_date, i['city'])
        try:
            if flight.price < i['lowestPrice']:
                dest_city = str(flight.dest_city).split("'")[1]
                notification_manager.send_notification(dest_city, flight.price)
        except AttributeError:
            continue


# Initialize objects.
data_manager = DataManager(SHEETY_ENDPOINT, SHEETY_TOKEN)
flight_searcher = FlightSearch(KIWI_API_KEY, KIWI_ENDPOINT)
notification_manager = NotificationManager(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN, SOURCE_PHONE_NUMBER, DEST_PHONE_NUMBER)

#sheet_data = (data_manager.get_iata_data())
# Uncomment to test without having to make calls to sheety - free account only gets 200 API calls a month.
sheet_data = [
    {'city': 'Seoul', 'iataCode': 'ICN', 'lowestPrice': 0, 'id': 2},
    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 0, 'id': 3},
    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 0, 'id': 4},
    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 0, 'id': 5},
    {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 0, 'id': 6},
    {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 0, 'id': 7},
    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 0, 'id': 8},
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 0, 'id': 9},
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 5000, 'id': 10},
    {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 0, 'id': 11},
]

update_iata_column(sheet_data)
search_for_flights(sheet_data)