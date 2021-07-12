from bs4 import BeautifulSoup
import requests

target_url = "https://blog.teddykatz.com/2019/11/12/github-actions-dos.html"

def write_hrefs(links_scraped):
    with open('scraped_links.txt', mode='wt', encoding='utf-8') as output:
        output.write('\n'.join(links_scraped))

response = requests.get(target_url)
text = (response.text)

soup = BeautifulSoup(text, 'html.parser')

anchors = soup.findAll(name='a')
stringed_anchors = [str(tag['href']) for tag in anchors]
href_list = [tag for tag in stringed_anchors if tag[0:4] == 'http']

write_hrefs(href_list)