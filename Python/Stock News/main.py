import requests
from decouple import config
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_KEY = config("ALPHAVANTAGE_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = config("NEWS_API_KEY", default='')
TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID", default='')
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN", default='')
TWILIO_FROM_NUMBER = config("TWILIO_FROM_NUMBER", default='')
TWILIO_TO_NUMBER = config("TWILIO_TO_NUMBER", default='')


def form_sms_body(percentage_difference: float, stock: str, news_data_dict: {}) -> str:
    news_body_sms = ""
    for curr_news in news_data_dict:
        for key, value in curr_news.items():
            news_body_sms += f"Headline: {key}\nBrief: {value}\n\n"
    if percentage_difference >= 0:
        body_sms = f"{stock}: 🔺{percentage_difference}\n\n+{news_body_sms}"
    else:
        body_sms = f"{stock}: 🔻{percentage_difference}\n\n+{news_body_sms}"
    return body_sms


params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY
}

# GET STOCK CLOSE PRICE FOR THE LAST TWO DAYS AND CALCULATE PERCENTAGE DIFFERENCE
response = requests.get(ALPHAVANTAGE_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
last_two_days_close_data = [float(data[key]["4. close"]) for key in list(data)[:2]]

percentage_diff = (last_two_days_close_data[0] - last_two_days_close_data[1]) * 100 / last_two_days_close_data[1]
news_data = []
percentage_diff = -10
# IF THE % DIFF IS + OR -5 FETCH NEWS AND SEND ALERT TO THE USER
if percentage_diff >= 5 or percentage_diff <= -5:
    # GET NEWS ARTICLES
    news_params = {
        "q": STOCK,
        "from": list(data)[0],
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_API_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_list = news_response.json()["articles"][:3]

    news_data = [{news["title"]: news["description"]} for news in news_list]

    # SEND SMS USING TWILIO
    sms_body = form_sms_body(percentage_difference=percentage_diff, stock=STOCK, news_data_dict=news_data)

    # TWILIO FOR SENDING ALERTS
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=sms_body,
        from_=TWILIO_FROM_NUMBER,
        to=TWILIO_TO_NUMBER
    )

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
