import requests

class DataManager:
    def __init__(self, sheety_endpoint, sheety_token):
        self.sheety_headers = {
            "Authorization": f"Bearer {sheety_token}"
        }
        self.sheety_endpoint = sheety_endpoint


    def get_iata_data(self):

        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
        prices = response.json()['prices']

        return prices

    def edit_iata_data(self, object_endpoint, post_parameters):

        response = requests.put(url=object_endpoint, json=post_parameters, headers=self.sheety_headers)
        
        return response.text