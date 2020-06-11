from player_1 import Player, Pitcher
import csv

#Player test
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

#Pitcher test
f = open('player_record/pitcher19.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)

pitcher19_list = list()

i = 0

for line in lines:
    if i > 0:
        pitcher19_list.append(Pitcher(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18]))
        i += 1
    else: 
        i += 1

for pitcher in pitcher19_list:
    print(pitcher)

f.close()