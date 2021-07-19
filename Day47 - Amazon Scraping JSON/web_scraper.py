import requests
from bs4 import BeautifulSoup


class WebScraper:

    def retrieve_price_from_site(self, target_product, preferred_price):

        request_header = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67'
        }

        response = requests.get(target_product, headers=request_header)

        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        price = float(soup.find(name='span', id='price').getText().strip('$'))
        name = soup.find(name='span', id='productTitle').getText()
        url = soup.find('link', {'rel':'canonical'})['href']
        target_price = preferred_price

        product_dict = {
            "Product Name": name.strip('\n'),
            "Price": price,
            "Target Price": target_price,
            "URL": url,
        }

        return product_dict