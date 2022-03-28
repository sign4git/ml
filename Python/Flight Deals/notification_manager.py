from flight_data import FlightData
from twilio.rest import Client
from decouple import config

TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID", default="")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default="")
TWILIO_FROM_NUMBER = config("TWILIO_FROM_NUMBER", default="")
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER", default="")


class NotificationManager:
    def __init__(self, flight_data: FlightData):
        self.notify_data = flight_data

    def notify_user(self):
        sms_body = f"Low Price Alert!! Only £{self.notify_data.price} to fly from " \
                   f"{self.notify_data.destination_city}-{self.notify_data.destination_airport}" \
                   f"from {self.notify_data.out_date} to {self.notify_data.return_date}"

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        client.messages \
            .create(
            body=sms_body,
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER
        )
