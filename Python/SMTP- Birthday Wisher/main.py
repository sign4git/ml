import os
import pandas as pd
import datetime as dt
import random
import smtplib
from decouple import config

username = config('user', default='')
password = config('password', default='')

birthday_data = pd.read_csv("birthdays.csv")
birthday_list = birthday_data.to_dict(orient="records")

letter_templates = []
for (dir_path, dir_names, filenames) in os.walk("letter_templates"):
    letter_templates += [os.path.join(dir_path, file) for file in filenames]

now = dt.datetime.now()
today_day = now.day
today_month = now.month

for current_person in birthday_list:
    if today_day == current_person["day"] and today_month == current_person["month"]:
        letter = random.choice(letter_templates)
        with open(letter, "r") as file:
            data = file.read()
            data = str(data).replace('[NAME]', current_person["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=username, password=password)
                connection.sendmail(from_addr=username, to_addrs=current_person['email'],
                                    msg=f"Subject:Happy Birthday {current_person['name']}\n\n {data}")
