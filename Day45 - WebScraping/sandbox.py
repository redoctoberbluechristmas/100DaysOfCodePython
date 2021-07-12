from bs4 import BeautifulSoup


with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

all_a = soup.findAll(name="a")
#print(all_a)

links = []

for tag in all_a:
    # 1. Option 1.
    link = tag.get("href")
    # 2. Option 2.
    #link = tag['href']
    links.append(link)

heading = soup.find(name="h1", id="name")  #<--- use to grab one specific h1, among bunches of h1s
other_pages = (soup.find(name="h3", class_="heading")).text
print(other_pages)

