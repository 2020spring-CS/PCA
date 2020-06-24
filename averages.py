#순위예측 비교를 위한 다른 방식들
#2017-2019 결과 기반 2020 결과 예측

from player_1 import Player, Record_Hitter, Record_Pitcher
import csv

#player_list
player_list = list()
player_names = list()

f = open('player_record/player19.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)
record19 = []
for line in lines:
    record19.append(line)

f.close()

i = 0
for record in record19:
    if i > 0:
        if record[1] in player_names:
            pass
        else: 
            player_list.append(Player(record[1], record[2], 'Hitter'))
            player_names.append(record[1])
            i += 1
    else: 
        i += 1

for player in player_list:
    for record in record19:
        if player.name == record[1]:
            player.update(Record_Hitter(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], 2019))

#산술평균
#airthmetic mean
Doosan = [[], 0]
Hanhwa = [[], 0]
Kia = [[], 0]
Kiwoom = [[], 0]
KT = [[], 0]
LG = [[], 0]
Lotte = [[], 0]
NC = [[], 0]
Samsung = [[], 0]
SK = [[], 0]

for player in player_list:
    if player.team == '두산':
        Doosan[0].append(player)
        Doosan[1] += 1
    elif player.team == 'NC':
        NC[0].append(player)
        NC[1] += 1
    elif player.team == 'LG':
        LG[0].append(player)
        LG[1] += 1
    elif player.team == '키움' or player.team == '넥센':
        Kiwoom[0].append(player)
        Kiwoom[1] += 1
    elif player.team == 'LG':
        LG[0].append(player)
        LG[1] += 1
    elif player.team == 'KT':
        KT[0].append(player)
        KT[1] += 1
    elif player.team == 'KIA':
        Kia[0].append(player)
        Kia[1] += 1    
    elif player.team == '롯데':
        Lotte[0].append(player)
        Lotte[1] += 1   
    elif player.team == '삼성':
        Samsung[0].append(player)
        Samsung[1] += 1  
    elif player.team == '한화':
        Hanhwa[0].append(player)
        Hanhwa[1] += 1    

def arithmetic_mean(team):
    X = [player.record[0].AVG for player in team[0] for i in range(team[1])]
    return sum(X) / team[1]

#Weighted Arithmetic Mean
#p-values를 scipy 없이 구현하지 못할 경우 k-means로 대체
X= [[player.record[i].AVG, player.record[i].XBH, player.record[i].GO, player.record[i].AO, player.record[i].GW_RBI, player.record[i].BB_K, player.record[i].P_PA, player.record[i].ISOP, player.record[i].XR, player.record[i].GPA]
 for i in range(len(player.record)) for player in player_list]

P = [[stat/X[i][0] for stat in X[i]] for i in range(len(X))]

