import numpy as np
import matplotlib.pyplot as plt

from player_1 import Player, Record_Hitter, Record_Pitcher
import csv

#make list of players
player_list = list()
player_names = list()

#2018
f = open('player_record/player18.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)
record18 = []
for line in lines:
    record18.append(line)

f.close()

i = 0
for record in record18:
    if i > 0:
        player_list.append(Player(record[1], record[2], 'Hitter'))
        player_names.append(record[1])
        i += 1
    else: 
        i += 1

for player in player_list:
    for record in record18:
        if player.name == record[1]:
            player.update(Record_Hitter(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], 2018))

#check
for player in player_list:
    player.print()

#2019
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

#check
for player in player_list:
    player.print()

'''
Players are in player_list in the form of [[양의지18], [양의지19]]
'''

#code from pca_1.ipynb

#Using list comprehension
X= [[player.record[i].AVG, player.record[i].XBH, player.record[i].GO, player.record[i].AO, player.record[i].GW_RBI, player.record[i].BB_K, player.record[i].P_PA, player.record[i].ISOP, player.record[i].XR, player.record[i].GPA]
 for i in range(len(player.record) - 1) for player in player_list]

X_std= (X-np.mean(X, axis=0))/ np.std(X, axis=0)
mean_vec= np.mean(X_std, axis=0)

cov_mat=np.cov(X_std.T)
eig_values, eig_vectors = np.linalg.eig(cov_mat) #error not solved yet


idx= np.argsort(eig_values)[::-1]
eig_values=eig_values[idx]
eig_vectors=eig_vectors[:,idx]

#Find proper dimension
explained_var = [(t/sum(eig_values))*100 for t in sorted(eig_values, reverse=True)]
cum_explained_var= np. cumsum(explained_var)

#Explain 96% of variation with 6-dimension
a6= np.dot(X_std, eig_vectors[:,:6])
a5= np.dot(X_std, eig_vectors[:,:5])
a4= np.dot(X_std, eig_vectors[:,:4])
a3= np.dot(X_std, eig_vectors[:,:3])
a2= np.dot(X_std, eig_vectors[:,:2])
a1= np.dot(X_std, eig_vectors[:,:1])

fig=plt.figure(figsize=(5,5))
axis = fig.add_subplot(111)
axis.set_title('2 component PCA')
axis.grid(True)

plt.scatter(a2[:,0], a2[:, 1])
plt.show()
