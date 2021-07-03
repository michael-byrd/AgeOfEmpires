import csv
import requests

url = f"https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591"
resp = requests.get(url).json()
lastmatch = resp['last_match']
players = []


class Player:
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.country = ''
        self.tg_rating = 0
        self.rating = 0

    def info(self):
        player_url = f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=4"
        player_url_1v1 = f"https://aoe2.net/api/leaderboard?game=aoe2de&profile_id={self.id}&leaderboard_id=3"
        player_tg = requests.get(player_url).json()
        player_1v1 = requests.get(player_url_1v1).json()
        player_tg_rating_url = f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=4&profile_id={self.id}&count=1"
        player_tg_rate = requests.get(player_tg_rating_url).json()
        player_1v1_rating_url =f"https://aoe2.net/api/player/ratinghistory?game=aoe2de&leaderboard_id=3&profile_id={self.id}&count=1"
        player_1v1_rate = requests.get(player_1v1_rating_url).json()

        if len(player_tg["leaderboard"]) > 0:
            playerLeaderboard = player_tg["leaderboard"][0]
            self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1["leaderboard"]) > 0:
            playerLeaderboard = player_1v1["leaderboard"][0]
            self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1_rate) > 0:
            self.rating = player_1v1_rate[0]['rating']
        if len(player_tg_rate) > 0:
            self.tg_rating = player_tg_rate[0]['rating']


    @property
    def print_info(self):
        return ("Name: " + str(self.name) + "\n\tCountry: " + str(self.country) + "\tTG ELO:" + str(self.tg_rating) + "\tELO: " + str(self.rating) + '\n')

def getPlayerIDs():
    for player in lastmatch['players']:
        # profileIDs.append(player['profile_id'])
        players.append(Player(player['profile_id']))

getPlayerIDs()
for player in players:
    player.info()
    print(player.print_info)
