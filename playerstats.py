from __future__ import print_function
import sys
sys.path.append("~/code/nba_py/")
from nba_py import league
import time
from datetime import date
import json
import csv
import json
import csv

# endpoint currently disabled on stats.nba.com
# pd = player._PlayerDashboard('203507')
# print(pd.starting_position())

ap = league.PlayerStats()
tp = league.TeamStats()
print(tp.overall)
date = date.today()


# setup team csv

with open("teamdata{0}.json".format(date), 'w') as outfile:
	json.dump(tp.overall(), outfile, indent=4, sort_keys=True, separators=(',', ':'))


with open("teamdata{0}.json".format(date)) as team_data_file:    
    teams_parsed = json.load(team_data_file)


# open a file for writing
teams_data = open("teamdatafor{0}.csv".format(date), 'w')

# create the csv writer object

teamcsvwriter = csv.writer(teams_data)

count = 0

for team in teams_parsed:
	if count == 0:
		header = team.keys()
		teamcsvwriter.writerow(header)
		count +=1
	teamcsvwriter.writerow(team.values())

teams_data.close()




with open("playerdata{0}.json".format(date), 'w') as outfile:
	json.dump(ap.overall(), outfile, indent=4, sort_keys=True, separators=(',', ':'))


with open("playerdata{0}.json".format(date)) as data_file:    
    player_parsed = json.load(data_file)


# open a file for writing
player_data = open("playerdatafor{0}.csv".format(date), 'w')

# create the csv writer object

csvwriter = csv.writer(player_data)

count = 0

for player in player_parsed:
	if count == 0:
		header = player.keys()
		csvwriter.writerow(header)
		count +=1
	csvwriter.writerow(player.values())

player_data.close()


