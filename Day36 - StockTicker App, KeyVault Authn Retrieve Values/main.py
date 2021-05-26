import os
import requests
from twilio.rest import Client
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#KeyVault authentication using environment variables.

keyvault_url = os.environ.get('KEYVAULT_URL')
credential = DefaultAzureCredential()
client = SecretClient(keyvault_url, credential)


# Stock to search
STOCK = "MSFT"
COMPANY_NAME = "Microsoft"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Retrieving API secrets from Key Vault
stock_api_key = client.get_secret("stock-api-key").value
news_api_key = client.get_secret("news-api-key").value
sms_account_sid = client.get_secret("sms-account-sid").value
sms_auth_token = client.get_secret("sms-auth-token").value

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key,
}

stock_request = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_request.raise_for_status()
stock_data = stock_request.json()["Time Series (Daily)"]

# stock_data is a dictionary, with days for keys and each day a dictionary of associated values. By adding the
# value dictionaries to a list, you can now iterate through and grab what you need from the dictionaries.

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_closing = float(stock_data_list[0]['4. close'])
day_before_closing = float(stock_data_list[1]['4. close'])
compare_y_day_before = yesterday_closing - day_before_closing

if compare_y_day_before > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

# use abs, because I want to be notified if greater than 5% change in either direction.
percent_diff = abs(round((compare_y_day_before) / day_before_closing * 100, 2))

# Will send text message to dest_phone_number with news articles if stock changes 5% or more in one day.
if percent_diff >= 5:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": news_api_key,
    }

    news_request = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_request.raise_for_status()
    news_data = news_request.json()['articles']

    first_3_articles = news_data[:3]

    formatted_articles_list = [f"{STOCK}: {arrow}{percent_diff}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_3_articles]
    twilio_client = Client(sms_account_sid, sms_auth_token)

    source_phone_number = client.get_secret('source-phone-number').value
    dest_phone_number = client.get_secret('dest-phone-number').value

    for article in formatted_articles_list:
        twilio_client.messages.create(
            body=article,
            from_=source_phone_number,
            to=dest_phone_number
        )
else:
    print("No major day-on-day change.")