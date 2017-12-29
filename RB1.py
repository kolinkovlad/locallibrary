import requests
from bs4 import BeautifulSoup

j = 0
data_1 = ""
for i in range (1,2):

    url = ('https://minjust.gov.ua/news/page/{0}'.format(i))
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for i in soup.find_all("article", {"class":'grid-item col-sm-4'}):
        z = i.find_all("a")
        for p in z:
            data_1 += str(j) +'\t'  + i.div.span.text + '\t'  + i.h5.text + '\t' + 'https://minjust.gov.ua'+ p['href'] + "\n"
            j += 1
            print(str(j) +'\t'  + i.div.span.text + '\t'  + i.h5.text + '\t' + 'https://minjust.gov.ua'+ p['href'] + "\n")



f = open('minjust.txt', 'w')
f.write(data_1)
f.close()

