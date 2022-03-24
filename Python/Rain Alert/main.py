import requests
from twilio.rest import Client
# import os
from decouple import config

# from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

# TWILIO SID AND TOKEN
TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")
OPEN_WEATHER_APPID = config("OPEN_WEATHER_APPID")
TWILIO_FROM_NUMBER = config("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER")

bring_an_umbrella_flag = False
parameters = {
    "lat": 9.925201,
    "lon": 78.119774,
    "appid": OPEN_WEATHER_APPID,
    "exclude": "daily,minutely,current"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
hourly_forecast = response.json()["hourly"][:12]
for next_forecast in hourly_forecast:
    if not bring_an_umbrella_flag:
        if next_forecast["weather"][0]["id"] < 700:
            bring_an_umbrella_flag = True
    else:
        print("Bring an umbrella")
        break

# TWILIO FOR SENDING ALERTS
if bring_an_umbrella_flag:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body="Hello There!! It's going to rain today. Please do not forgot to bring an Umbrella",
        from_=TWILIO_FROM_NUMBER,
        to=TWILIO_TO_NUMBER
    )

    print(message)
    print(message.sid)
    print(message.status)
