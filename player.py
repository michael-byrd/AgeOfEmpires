#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import requests
import sys

# while True:
url = f"https://aoe2.net/api/player/lastmatch?game=aoe2de&profile_id=313591" #313591 5001328
resp = requests.get(url).json()
lastmatch = resp['last_match']
playerName = resp['name']
print(playerName)
players = []
team1 = []
team2 = []
hammerTeam1 = False
hammerTeam2 = False


class Player:
    def __init__(self, id, team, color, name):
        self.id = id
        self.team = team
        self.color = color
        self.name = name
        self.country = '--'
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
            # self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1["leaderboard"]) > 0:
            playerLeaderboard = player_1v1["leaderboard"][0]
            # self.name = playerLeaderboard["name"]
            self.country = playerLeaderboard["country"]
        if len(player_1v1_rate) > 0:
            self.rating = player_1v1_rate[0]['rating']
        if len(player_tg_rate) > 0:
            self.tg_rating = player_tg_rate[0]['rating']

    @property
    def print_info(self):
        return ("Name: " + str(self.name) + "\n\tCountry: " + str(self.country) + "\tTG ELO:" + str(self.tg_rating) + "\tELO: " + str(self.rating) + '\tTEAM: ' + str(self.team) + '\n')

def getPlayerIDs():
    for player in lastmatch['players']:
        # profileIDs.append(player['profile_id'])
        players.append(Player(player['profile_id'], player['team'], player['color'], player['name']))
    for player in players:
        if player.team == 1:
            team1.append(player)
        elif player.team == 2:
            team2.append(player)
count = 0
with open('index2.html', 'w', encoding="utf-8") as info:
    info.truncate()
    getPlayerIDs()
    for player in players:
        player.info()
        if (player.name == playerName) and player.team == 1:
            hammerTeam1 = True
        elif (player.name == playerName) and player.team == 2:
            hammerTeam2 = True
        count += 1
    print("Team1", hammerTeam1)
    print("Team2", hammerTeam2)
    print("<!DOCTYPE html>\n<html>\n"+'<meta http-equiv="refresh" content="2">\n<meta charset="utf-8">'+"\n<head>\n\n</head>\n<body>\n<table>", file = info)
    if hammerTeam1 == True:
        for i in range(count // 2):
            player1 = team1[i]
            player2 = team2[i]
            print('<tr><td>' + str(player1.name) + '</td><td>' + str(player1.country) + '</td><td>' + str(player1.tg_rating) + "</td><td style='padding-right:15px;'>" + str(player1.rating) + '</td>', file=info)
            print('<td>' + str(player2.rating) + '</td><td>' + str(player2.tg_rating) + '</td><td>' + str(player2.country) + '</td><td>' + str(player2.name) + '</td></tr>', file=info)
    elif hammerTeam2 == True:
        for i in range(count // 2):
            player1 = team2[i]
            player2 = team1[i]
            print('<tr><td>' + str(player1.name) + '</td><td>' + str(player1.country) + '</td><td>' + str(player1.tg_rating) + "</td><td style='padding-right:15px;'>" + str(player1.rating) + '</td>', file=info)
            print('<td>' + str(player2.rating) + '</td><td>' + str(player2.tg_rating) + '</td><td>' + str(player2.country) + '</td><td>' + str(player2.name) + '</td></tr>', file=info)
    else:
        for i in range(count // 2):
            player1 = team1[i]
            player2 = team2[i]
            print('<tr><td>' + str(player1.name) + '</td><td>' + str(player1.country) + '</td><td>' + str(player1.tg_rating) + "</td><td style='padding-right:15px;'>" + str(player1.rating) + '</td>', file=info)
            print('<td>' + str(player2.rating) + '</td><td>' + str(player2.tg_rating) + '</td><td>' + str(player2.country) + '</td><td>' + str(player2.name) + '</td></tr>', file=info)
    print('</table>\n</body>\n</html>', file=info)
