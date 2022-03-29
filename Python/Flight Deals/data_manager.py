import requests
from decouple import config

FLIGHT_DEALS_SHEETY_API = config("FLIGHT_DEALS_SHEETY_API", default="")
auth = (config("FLIGHT_DEALS_BASIC_AUTH_USER", default=''), config("FLIGHT_DEALS_BASIC_AUTH_PASS", default=''))
USER_FLIGHT_DEALS_SHEETY_API = config("USER_FLIGHT_DEALS_SHEETY_API", default="")


class DataManager:
    def __init__(self):
        self.price_data = {}
        self.user_data = {}

    def get_price_data(self) -> {}:
        google_sheet_response = requests.get(f"{FLIGHT_DEALS_SHEETY_API}", auth=auth)
        google_sheet_response.raise_for_status()
        self.price_data = google_sheet_response.json()["prices"]
        print(self.price_data)
        return self.price_data

    def update_iata_code(self):
        for city in self.price_data:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_sheet = requests.put(f"{FLIGHT_DEALS_SHEETY_API}/{city['id']}", auth=auth,
                                        json=parameters)
            update_sheet.raise_for_status()

    def get_users_data(self) -> {}:
        google_sheet_response = requests.get(f"{USER_FLIGHT_DEALS_SHEETY_API}", auth=auth)
        google_sheet_response.raise_for_status()
        self.user_data = google_sheet_response.json()["users"]
        return self.user_data

    def post_users_data(self, f_name, l_name, email):
        params = {
            "user": {
                'firstName': f_name,
                'lastName': l_name,
                'email': email
            }
        }
        google_sheet_response = requests.post(f"{USER_FLIGHT_DEALS_SHEETY_API}", auth=auth, json=params)
        google_sheet_response.raise_for_status()
        print(google_sheet_response.json())
        return self.user_data
