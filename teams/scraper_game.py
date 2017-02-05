import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "champsleague.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from teams.models import Team, Player, Game
from bs4 import BeautifulSoup
import requests


for i in range(20, 21):
    i+=1
    url = 'http://www.euroleague.net/main/results?gamenumber={}'.format(i)
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    livescore = soup('div', class_='livescore')[1]
    games = livescore.find_all('div', class_='game played')
    n = i*10
    for game in games:
        n+=1
        p = 'p' + str(n)
        game = game('div', class_='club')
        match_no = int(i)
        h_team = str(game[0].span.string)
        h_res = int(game[0].text.split(' ')[-1])
        a_team = str(game[1].span.string)
        a_res = int(game[1].text.split(' ')[-1])

        p = Game(round = match_no, home_team = Team.objects.get(name__icontains=h_team), home_result = h_res, away_team = Team.objects.get(name__icontains=a_team), away_result = a_res)
        p.save()
        print(match_no, h_team, h_res, a_team, a_res)

