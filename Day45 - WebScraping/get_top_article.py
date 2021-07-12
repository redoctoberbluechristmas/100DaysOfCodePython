from bs4 import BeautifulSoup
import requests
from datetime import datetime

now = datetime.now()
response = requests.get("https://news.ycombinator.com/news")

# Get HTML source
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')


def get_top_article(all_articles, list_to_sort):
    top_upvote_count = max(list_to_sort)
    top_upvote_index = list_to_sort.index(top_upvote_count)
    top_article_object = all_articles[top_upvote_index]
    return top_article_object

# Grab all of a category.
article_storylinks = soup.find_all(name='a', class_='storylink')
article_points = soup.find_all(name='span', class_='score')

titles = [tag.getText() for tag in article_storylinks]
links = [tag.get('href') for tag in article_storylinks]
upvotes = [int(tag.getText().split()[0]) for tag in article_points]

#Combining three lists into dictionaries.
article_list = [
    {
        'title': title,
        'link': link,
        'upvotes': upvotes
    } for title,link,upvotes in zip(titles, links, upvotes)
]

top_article = get_top_article(article_list, upvotes) # returns the dictionary of the top article.

print(f"The most popular article as of {datetime.now()} is '{top_article['title']}'\n"
      f"The link to the article is {top_article['link']}")
