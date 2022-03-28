import requests
from decouple import config

FLIGHT_DEALS_SHEETY_API = config("FLIGHT_DEALS_SHEETY_API", default="")
auth = (config("FLIGHT_DEALS_BASIC_AUTH_USER", default=''), config("FLIGHT_DEALS_BASIC_AUTH_PASS", default=''))


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self) -> {}:
        google_sheet_response = requests.get(f"{FLIGHT_DEALS_SHEETY_API}", auth=auth)
        google_sheet_response.raise_for_status()
        self.sheet_data = google_sheet_response.json()["prices"]
        return self.sheet_data

    def update_iata_code(self):
        for city in self.sheet_data:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_sheet = requests.put(f"{FLIGHT_DEALS_SHEETY_API}/{city['id']}", auth=auth,
                                        json=parameters)
            update_sheet.raise_for_status()
