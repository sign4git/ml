import requests
from flight_data import FlightData
from decouple import config

TEQUILA_KIWI_TRAVEL_API_KEY = config("TEQUILA_KIWI_TRAVEL_API_KEY", default="")
TEQUILA_FLIGHT_SEARCH_ENDPOINT = config("TEQUILA_FLIGHT_SEARCH_ENDPOINT", default="")
TEQUILA_LOCATION_QUERY = config("TEQUILA_LOCATION_QUERY", default="")
tequila_headers = {
    "apikey": TEQUILA_KIWI_TRAVEL_API_KEY
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.iata_code = None

    def get_iata_code(self, city: str):
        parameters = {
            "term": city,
            "location_types": "city"
        }
        get_iata_code_response = requests.get(TEQUILA_LOCATION_QUERY, headers=tequila_headers,
                                              params=parameters)
        get_iata_code_response.raise_for_status()
        self.iata_code = get_iata_code_response.json()["locations"][0]["code"]
        return self.iata_code

    def get_destination_city_and_price(self, destination_city_code: str, source_city_code: str, from_date: str,
                                       to_date: str):
        parameters = {
            "fly_from": source_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_date,
            "dateTo": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(TEQUILA_FLIGHT_SEARCH_ENDPOINT, params=parameters, headers=tequila_headers)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
