from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://kinoafisha.ua/ua/skoro/")
bs = BeautifulSoup(html, "html.parser")

for child in bs.find("div", {'class', 'item'}).children:
    element = child.find('h3')
    print(element, '\n')

for ch in bs.find('div', {'class', 'item'}).children:
    a = ch.find('b')
    print(a, '\n')

for bh in bs.find('div', {'class', 'text'}).children:
    b = bh.find('span')
    print(b, '\n')

for ch in bs.find('div', {'class', 'item'}).children:
    c = ch.find('img')
    print(c, '\n')

for kh in bs.find('div', {'class', 'text'}).children:
    k = kh.find('text')
    print(k, '\n')

q = str(element + a + b + c + k)

with open('info.txt', 'w') as f: #З записом проблема. 
    f.write(q) 