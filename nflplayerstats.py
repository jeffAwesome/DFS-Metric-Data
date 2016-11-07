from __future__ import print_function
from urllib2 import Request, urlopen, URLError
import nflgame
from nflgame import game
import json
import csv
import requests
import time
from datetime import date

date = date.today()

'''

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token token=ee1343e93b0153c0b6c84f891254b3dc',
    'Accept': 'application/vnd.stattleship.com; version=1',
}

data = requests.get('https://api.stattleship.com/football/nfl/team_season_stats', headers=headers)

print(data.json());

with open("nflteamdata{0}.json".format(date), 'w') as outfile:
	json.dump(data.json(), outfile, indent=4, sort_keys=True, separators=(',', ':'))

'''



nflgame.combine(nflgame.games(2016)).csv("nflplayerdata-{0}.csv".format(date))
