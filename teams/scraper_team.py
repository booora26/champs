import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "champsleague.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from teams.models import Team, Player
from bs4 import BeautifulSoup
import requests

url = 'http://www.euroleague.net/competition/teams'
source = requests.get(url)
soup = BeautifulSoup(source.content, 'lxml')

def team(link, img, var, var2):
    source= requests.get(link)
    soup = BeautifulSoup(source.content, 'lxml')

    name = soup.find('div', class_='title')
    name = str(name.text)
    teamdata = soup.find('div', class_='wp-module wp-module-teamdata wp-module-6322')
    address = teamdata.find_all('dd')[1].text
    country = address.split(' ')[-1]
    arena_address = teamdata.find_all('dd')[-1].contents
    arena = arena_address[0].string
    website = soup.find('li', class_='website')
    website = website.a.get('href')
    logo = img
    var = 'p' + str(var)
    var = Team(name=name, country=country, arena=arena, website=website, logo=logo)
    var.save()
    tag = soup.find_all('div', class_='item player')
    no = var2 * 100
    for player_info in tag:
        no += 1
        var3 = 'i' + str(no)
        try:
         full_name = player_info.a.img.get('alt')
         first_name = full_name.split(', ')[1]
         last_name = full_name.split(', ')[0]
         number = player_info.find('span', class_='dorsal').string
         number = int(number.split('#')[1])
         position = player_info.find('span', class_='position').string
         nationality = player_info.find('span', class_='country').string
         born = int(player_info.find('span', class_='birth').string)
         height = player_info.find('span', class_='height').string
         height = height.split('Height: ')[1]
         height = int(float(height) * 100)
         pic = player_info.div.a.img.get('src')
         var3 = Player(first_name=first_name, last_name=last_name, position=position, number=number, height=height,
         born=born, nationality=nationality, pic=pic, club=var)
         var3.save()
        except:
         continue
        print(first_name, last_name, position, number, height, born, nationality, pic)


tag = soup.find('div', class_=['teams'])
tag1 = tag.find_all('div', class_=['item'])
n = 0
for div1 in tag1:
    link = 'http://www.euroleague.net' + div1.a.get('href')
    img = div1.a.img.get('src')
    n +=1
    #var = 'p' + str(n) # za klubove
    var = n
    var2 = n
    team(link, img, var, var2)

# link = 'http://www.euroleague.net/competition/teams/showteam?clubcode=MIL&seasoncode=E2016'
# var = 26
# img = 'http://www.euroleague.net/rs/6am5uxxarbmybtyd/5fae8dff-b186-4e7f-a158-c16e8e479736/a94/filename/5fa.png'

