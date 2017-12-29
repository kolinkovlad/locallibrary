import requests
from bs4 import BeautifulSoup

url = ("https://kinoafisha.ua/ua/skoro/")
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

info = ""
for i in soup.find_all("div", {'class':"item"}):                #find name - teg <h3> and find img
    for z in i.find_all('div', {'class':"date"}):               #find date
        for z1 in i.find_all('div', {'class': "countries"}):    #find countries
            z2 = z1.text.split()

            for f in i.find_all("p"):                           #find actors
                f1 = f.text.split()
                if 'Актори:' in f1:
                    info += z.text + '\t' + i.h3.text + '\t' + "https://kinoafisha.ua"+i.a.img['src'] + '\t' + z2[0] + '\t' +  " ".join(f1) + "\n"
                    print(z.text + '\t' + i.h3.text + '\t' + "https://kinoafisha.ua"+i.a.img['src'] + '\t' + z2[0] + '\t' +  " ".join(f1))


f = open('kinoafisha.txt', 'w')
f.write(info)
f.close()
print("Документ: kinoafisha.txt записано")



