
# CamelCamelCamel - give price history of product.
# myhttpheader.com - see what your browser headers are.

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from data_manager import DataManager
from notification_manager import NotificationManager
import os
from web_scraper import WebScraper

keyvault_url = os.environ.get('KEYVAULT_URL')
credential = DefaultAzureCredential()
kv_client = SecretClient(keyvault_url, credential)

MY_EMAIL = kv_client.get_secret('fake-email').value
PASSWORD = kv_client.get_secret('fake-email-password').value
TARGET_EMAIL = kv_client.get_secret('target-email').value

target_product = input("Please enter the full url of the product you wish to search: ")
preferred_price = float(input("Please enter your target price: ").strip('$'))

scraper = WebScraper()

product_dict = scraper.retrieve_price_from_site(target_product, preferred_price)
data_manager = DataManager(product_dict)

data_manager.check_if_item_in_data_file()
products_to_buy = data_manager.check_if_price_below_target()

notification_manager = NotificationManager(MY_EMAIL, PASSWORD)

notification_manager.send_email(products_to_buy, TARGET_EMAIL)




