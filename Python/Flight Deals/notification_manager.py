from flight_data import FlightData
from twilio.rest import Client
from decouple import config
import smtplib
from data_manager import DataManager

TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID", default="")
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default="")
TWILIO_FROM_NUMBER = config("TWILIO_FROM_NUMBER", default="")
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER", default="")
SMTP_USER = config('SMTP_USER', default='')
SMTP_PASSWORD = config('SMTP_PASSWORD', default='')

data_sheet_manager = DataManager()
user_data = data_sheet_manager.get_users_data()


class NotificationManager:
    def __init__(self, flight_data: FlightData):
        self.notify_data = flight_data
        self.user_data = user_data
        self.sms_body = None

    def get_notification_message(self):
        self.sms_body = f"Low Price Alert!! Only {self.notify_data.price}GBP to fly from " \
                        f"{self.notify_data.origin_city}-{self.notify_data.destination_city}" \
                        f" from {self.notify_data.out_date} to {self.notify_data.return_date}. "

        if self.notify_data.stop_overs >= 1:
            self.sms_body += f"Flight has {self.notify_data.stop_overs} stop over, via {self.notify_data.via_city}"

    def notify_user(self):
        self.get_notification_message()
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        client.messages \
            .create(
            body=self.sms_body,
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER
        )

    def send_emails(self):
        self.get_notification_message()
        for user in user_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=SMTP_USER, password=SMTP_PASSWORD)
                connection.sendmail(from_addr=SMTP_USER, to_addrs=user['email'],
                                    msg=f"Subject:Flight Low Price Deals!!!\n\n {self.sms_body.encode('utf-8')}")
