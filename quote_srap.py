import requests
from bs4 import BeautifulSoup

url_start = url = 'http://quotes.toscrape.com'
items = []

while True:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    for card in soup.find_all("div", {"class": 'quote'}):
        item ={}
        text = card.find("span", {"class": "text"}).text
        item['text'] = text
        author = card.find('small', {'class':'author'}).text
        item['author'] = author
        tags = card.find_all('a',{'class':'tag'})
        tags = ', '.join([item.text for item in tags])
        item['tags']= tags
        items.append(item)

    # pprint(items)
    try:
        next_page = soup.find("li",{'class':'next'}).a['href']
        url = url_start + next_page
        print(url)
    except:
        break

with open('quotes.txt', 'w') as file:
    for item in items:
        file.write('{ ')
        for key in item.keys():
            file.write(key+" : "+item[key]+'| ')
        file.write("}\n")
