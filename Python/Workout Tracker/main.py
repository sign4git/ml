import requests
from decouple import config
import datetime as dt

# NUTRITIONIX TRACK API
APP_ID = config('APP_ID', default='')
APP_KEY = config('APP_KEY', default='')
POST_QUERY_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

# SHEETY API
SHEETY_ENDPOINT = config('SHEETY_ENDPOINT', default='')
SHEETY_BASIC_AUTH_USER = config('SHEETY_BASIC_AUTH_USER', default='')
SHEETY_BASIC_AUTH_PWD = config('SHEETY_BASIC_AUTH_PWD', default='')

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

QUERY = input("Tell me what exercise you did today with the details: ")

nutritionix_request_body = {
    "query": QUERY,
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 169,
    "age": 26
}

nutritionix_response = requests.post(url=POST_QUERY_URL, json=nutritionix_request_body, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
print(nutritionix_response.text)

# GET SHEET CONTENTS
sheety_get_response = requests.get(url=SHEETY_ENDPOINT, auth=(SHEETY_BASIC_AUTH_USER, SHEETY_BASIC_AUTH_PWD))
sheety_get_response.raise_for_status()
print(sheety_get_response.json())

# POST A NEW ROW IN THE SHEET
TIME_NOW = dt.datetime.now()
DATE = TIME_NOW.strftime('%d/%m/%Y')
TIME = str(TIME_NOW.time()).split('.')[0]

sheety_headers = {
    "Authorization": "Basic c210cDE5OTU6SEd5JGgmeClDNEIwJER3",
    "Content-Type": "application/json"
}

sheety_request_body = {
    "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": nutritionix_response.json()["exercises"][0]["name"],
        "duration": nutritionix_response.json()["exercises"][0]["duration_min"],
        "calories": nutritionix_response.json()["exercises"][0]["nf_calories"],
        "id": 2
    }
}

sheety_post_response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=sheety_request_body,
                                     auth=(SHEETY_BASIC_AUTH_USER, SHEETY_BASIC_AUTH_PWD))
sheety_post_response.raise_for_status()
print(sheety_post_response.json())
