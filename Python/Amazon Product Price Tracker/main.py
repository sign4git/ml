import requests
from bs4 import BeautifulSoup
import smtplib
from decouple import config
import lxml

# SMTP USER NAME AND PASSWORD
USER = config('user', default='')
PASSWORD = config('password', default='')

# GET AMAZON PRODUCT URL AND SET THRESHOLD PRICE (PRICE YOU WANT TO BUY THE PRODUCT FOR)
AMAZON_PRODUCT_URL = "https://www.amazon.in/dp/152309513X/?coliid=IQ9M89GQQI1S5&colid=39L4KU282OPS7&psc=1&ref_=lv_ov_lig_dp_it"
PRODUCT_THRESHOLD_PRICE = 200

# ADD HEADERS TO AVOID CAPTCHA
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}

# GET PRODUCT NAME AND CURRENT PRICE USING BEAUTIFUL SOUP
response = requests.get(AMAZON_PRODUCT_URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price_tag = soup.find(name="span", class_="a-size-base a-color-price a-color-price")
product_title_tag = soup.find(class_="a-size-extra-large", name="span")
price = float(price_tag.getText().split("₹")[1])
productName = product_title_tag.getText()

# IF THE CURRENT PRICE IS LESS THAN THE THRESHOLD PRICE SEND AN EMAIL
if price <= PRODUCT_THRESHOLD_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs="apr4test@mailinator.com", msg=f"Subject:Product at Discount\n\n"
                                                                                    f"The product {productName} is at a discounted price of {price}. To buy now click the link {AMAZON_PRODUCT_URL}")
