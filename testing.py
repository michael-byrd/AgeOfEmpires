# Age stuff

import csv
import requests

API_ROOT = "https://aoe2.net/api/leaderboard?game=aoe2de"

url = f"https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591"

resp = requests.get(url).json()

lastmatch = resp['last_match']

profileIDs = []

for player in lastmatch['players']:
    profileIDs.append(player['profile_id'])


for id in profileIDs:
    player_url = f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={id}&leaderboard_id=4"
    player = requests.get(player_url).json()
    playerLeaderboard = player["leaderboard"][0]
    # print(playerLeaderboard)
    playerName = playerLeaderboard["name"]
    playerCountry = playerLeaderboard["country"]
    playerELO = playerLeaderboard["rating"]
    print(playerName, playerELO, playerCountry)
