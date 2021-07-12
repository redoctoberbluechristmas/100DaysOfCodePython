from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests
import re

target_url = "https://www.empireonline.com/movies/features/best-movies-2/"
local_web_file = "./data/100_best_movies.html"
movies_list_file = "./data/best_100_movies.txt"



def get_web_page():
    # Create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to the needed webpage
    response = session.get(target_url)
    # Run JavaScript code on webpage, increase timeout to 30 seconds from default of 8 to deal with timeout errors.
    response.html.render(timeout=30)

    # Save the webpage to file
    with open(local_web_file, mode='w', encoding='utf-8') as output:
        output.write(response.html.html)

def read_web_file():
    try:
        open(local_web_file)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from the file
        with open(local_web_file, mode='r', encoding='utf-8') as input:
            content = input.read()
        return BeautifulSoup(content, 'html.parser')

def write_movies_to_file(list_of_movies):
    with open(movies_list_file, mode='w', encoding='utf-8') as list_output:
        for i in list_of_movies:
            list_output.write(f"{i}\n")


# Checks if local web file of scraped content exists; if not, it loads it from the Internet.
soup = read_web_file()

h3h3 = soup.find_all(name='h3', class_='jsx-4245974604')

list = [tag.text for tag in h3h3]
reversed_list = list[::-1]
write_movies_to_file(reversed_list)


