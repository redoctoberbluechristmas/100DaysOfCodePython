import csv
from collections import Counter
import requests
import re

target_url = "https://blog.teddykatz.com/2019/11/12/github-actions-dos.html"
response = requests.get(target_url)
page_text = response.text

def strip_html(some_website_text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', some_website_text)

def scrub_dumb_words(list_to_scrub):
    scrubbed_list = []

    with open('dumb_words.csv', 'r') as input:
        reader = csv.reader(input)
        dumb_words_list = list(reader)[0]

        for i in list_to_scrub:
            if i not in dumb_words_list:
                scrubbed_list.append(i)
    return scrubbed_list


def get_word_count(some_website_text):
    some_website_text = some_website_text.lower()
    some_website_text = some_website_text.split()
    some_website_text = [i for i in some_website_text if i.isalpha()]
    some_website_text = scrub_dumb_words(some_website_text)
    some_website_text = Counter(some_website_text)
    some_website_text = dict(some_website_text)
    return some_website_text

def get_most_common_word(word_count_dict):
    words = list(word_count_dict.keys())
    counts = list(word_count_dict.values())
    high_count = max(counts)
    high_count_word = words[high_count]
    return {"word": high_count_word, "count": high_count}


def get_top_article(all_articles, list_to_sort):
    top_upvote_count = max(list_to_sort)
    top_upvote_index = list_to_sort.index(top_upvote_count)
    top_article_object = all_articles[top_upvote_index]
    return top_article_object

word_count_dict = get_word_count(page_text)
cw = get_most_common_word(word_count_dict)

print(f"The most common word on the page {target_url} right now is '{cw['word']}' with a count of {cw['count']}")


