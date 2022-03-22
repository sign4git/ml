import smtplib
from decouple import config

username = config('user', default='')
password = config('password', default='')
to_address = config('to_address', default='')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=username, password=password)
    connection.sendmail(from_addr=username, to_addrs=to_address, msg="Subject:This is my email from "
                                                                     "SMTP \n\n I am writing this "
                                                                     "email to test SMTP module from "
                                                                     "Python")
