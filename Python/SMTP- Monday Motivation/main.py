import smtplib
from decouple import config
import datetime as dt
import random

username = config('user', default='')
password = config('password', default='')
to_address = config('to_address', default='')

with open("quotes.txt", "r") as file:
    data = file.readlines()

quote_of_the_day = random.choice(data)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=to_address, msg="Subject:Monday Motivation "
                                                                         "Quote \n\n " + quote_of_the_day)
