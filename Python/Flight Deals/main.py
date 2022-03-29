from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from dateutil.relativedelta import relativedelta
from notification_manager import NotificationManager

START_DATE = (dt.datetime.now() + dt.timedelta(1)).strftime("%d/%m/%Y")
END_DATE = (dt.datetime.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
CURR = "GBP"

data_sheet_manager = DataManager()
sheet_data = data_sheet_manager.get_price_data()

for row in sheet_data:
    if len(row["iataCode"]) == 0 or row["iataCode"] == "":
        city = row["city"]
        flightSearch = FlightSearch()
        row["iataCode"] = flightSearch.get_iata_code(city=row["city"])
        data_sheet_manager.price_data = sheet_data
        data_sheet_manager.update_iata_code()

source_city = input("Enter your city: ")
flightSearch = FlightSearch()
source_city_code = flightSearch.get_iata_code(source_city)

for row in sheet_data:
    destination_city_code = row["iataCode"]
    destination_city = row["city"]
    if destination_city_code != source_city_code:
        flight_data = flightSearch.get_destination_city_and_price(source_city_code=source_city_code,
                                                                  destination_city_code=destination_city_code,
                                                                  from_date=START_DATE, to_date=END_DATE,
                                                                  destination_city=destination_city)
        try:
            if flight_data.price <= row["lowestPrice"]:
                notification_manager = NotificationManager(flight_data=flight_data)
                notification_manager.notify_user()
                notification_manager.send_emails()
        except AttributeError:
            print("No flight found")


