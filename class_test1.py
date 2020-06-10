from player_1 import Player
import csv

f = open('player_record/player19.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)

player19_list = list()

i = 0

for line in lines:
    if i > 0:
        player19_list.append(Player(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13]))
        i += 1
    else: 
        i += 1

for player in player19_list:
    print(player)

f.close()