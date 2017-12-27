from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://kinoafisha.ua/ua/skoro/")
bs = BeautifulSoup(html, "html.parser")

cards = bs.findAll("div", {'class': 'item'})

for i, card in enumerate(cards):

    # print(card.div.h3.text)
    title = card.div.h3.text

    actors = card.div.p.text

    # div.text
    # p
    #
    print(actors)
    # card = BeautifulSoup(card)
    date = card.find("div", {'class':'date'}).text
    image = card.find('img').get("src")
    # print(i, title, date, image)

# for child in bs.find("div", {'class', 'item'}).children:
#     element = child.find('h3')
#     print(element, '\n')
#
# for ch in bs.find('div', {'class', 'item'}).children:
#     a = ch.find('b')
#     print(a, '\n')
#
# for bh in bs.find('div', {'class', 'text'}).children:
#     b = bh.find('span')
#     print(b, '\n')
#
# for ch in bs.find('div', {'class', 'item'}).children:
#     c = ch.find('img')
#     print(c, '\n')
#
# for kh in bs.find('div', {'class', 'text'}).children:
#     k = kh.find('text')
#     print(k, '\n')
#
# q = str(element + a + b + c + k)
# print(q)
#
# with open('info.txt', 'w') as f: #З записом проблема.
#     f.write(q)