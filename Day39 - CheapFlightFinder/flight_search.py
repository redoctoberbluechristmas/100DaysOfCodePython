import os
import requests
from flight_data import FlightData
from datetime import datetime, timedelta



#https://tequila.kiwi.com/portal/my-solutions
#https://docs.kiwi.com/#header-searching-flights-and-connections-with-kiwi.com-(search-api)
class FlightSearch:
    def __init__(self, kiwi_api_key, kiwi_endpoint):
        self.kiwi_header = {
            "apikey": kiwi_api_key
        }
        self.kiwi_endpoint = kiwi_endpoint

    def get_iata_code(self, city):
        iata_query_endpoint = f"{self.kiwi_endpoint}/locations/query"
        iata_query_params = {
            "term": city,
            "location_types": "city"
        }

        response = requests.get(url=iata_query_endpoint, headers=self.kiwi_header, params=iata_query_params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def find_flights(self, src_city_iata, dest_city_iata, tomorrow_date, to_date, city_name):

        flight_search_endpoint = f"{self.kiwi_endpoint}/v2/search"
        flight_search_params = {
            "fly_from": src_city_iata,
            "fly_to": dest_city_iata,
            "date_from": tomorrow_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 10,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=flight_search_endpoint,
            headers=self.kiwi_header,
            params=flight_search_params,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            return (f"No flights found for {city_name}")

        flight_data = FlightData(
            price=data['price'],
            src_city=data['route'][0]['cityFrom'],
            src_airport=data['route'][0]['flyFrom'],
            dest_city=data['route'][0]['cityTo'],
            dest_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0],
        )

        #print(f"{flight_data.dest_city} for {flight_data.price}.")
        return flight_data
