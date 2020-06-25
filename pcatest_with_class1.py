import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

from player_1 import Player, Record_Hitter, Record_Pitcher
import csv

#2018
f = open('player_record/player18.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)
record18 = [line for line in lines]
f.close()

player_list = [Player(record[1], record[2], 'Hitter') for record in record18[1:]]
player_names = [record[1] for record in record18[1:]]

for player in player_list:
    for record in record18:
        if player.name == record[1]:
            player.update(Record_Hitter(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], 2018))

#check
#for player in player_list:
#    player.print()

#2019
f = open('player_record/player19.csv', 'rt', encoding='UTF8')
lines = csv.reader(f)
record19 = [line for line in lines]
f.close()

player_list = [Player(record[1], record[2], 'Hitter') for record in record19[1:]]
player_names = [record[1] for record in record19[1:]]

for player in player_list:
    for record in record19:
        if player.name == record[1]:
            player.update(Record_Hitter(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13], 2019))

#check
#for player in player_list:
#    player.print()

'''
Players are in player_list in the form of [[양의지18], [양의지19]]
'''

X= [[player.record[i].AVG, player.record[i].XBH, player.record[i].GO, player.record[i].AO, player.record[i].GW_RBI, player.record[i].BB_K, player.record[i].P_PA, player.record[i].ISOP, player.record[i].XR, player.record[i].GPA]
 for i in range(len(player.record)) for player in player_list]

X_std= (X-np.mean(X, axis=0))/ np.std(X, axis=0)
mean_vec= np.mean(X_std, axis=0)

cov_mat=np.cov(X_std.T)
eig_values, eig_vectors = np.linalg.eig(cov_mat)

idx= np.argsort(eig_values)[::-1]
eig_values=eig_values[idx]
eig_vectors=eig_vectors[:,idx]

#Find the proper dimension whose marginal explained variance is less than 5% 
explained_var = [(t/sum(eig_values))*100 for t in sorted(eig_values, reverse=True)]
cum_explained_var= np. cumsum(explained_var)

result = filter(lambda x: x<=5, explained_var)

final_dimension=explained_var.index(list(result)[0])+1
final_PCA = np.dot(X_std, eig_vectors[:,:final_dimension])

#Visualization PCA on 2-dimension
a3= np.dot(X_std, eig_vectors[:,:3])
a2= np.dot(X_std, eig_vectors[:,:2])
a1= np.dot(X_std, eig_vectors[:,:1])

fig=plt.figure(figsize=(5,5))
axis = fig.add_subplot(111)
axis.scatter(a2[:,0], a2[:,1])

axis.set_xlabel("PC1")
axis.set_ylabel("PC2")
axis.set_title('PCA with 2-dimension')
axis.grid(True)
plt.show()
print("Eigen Vectors with player records, Explaining {0}% \n PC1 : {1} with player records,\n PC2 : {2}".format(cum_explained_var[0], eig_vectors[:,:1], eig_vectors[:,1:2]))

#3-dimension
fig=plt.figure(figsize=(8,8))
axis = fig.add_subplot(111, projection='3d')
axis.scatter(a3[:,0], a3[:,1], a3[:,2])

axis.set_xlabel("PC1")
axis.set_ylabel("PC2")
axis.set_zlabel("PC3")

axis.set_title('PCA with 3-dimension')
axis.grid(True)
plt.show()
print("Eigen Vectors with player records, Explaining {0}% \n PC1 : {1},\n PC2 : {2},\n PC3:{3}".format(cum_explained_var[1],eig_vectors[:,:1], eig_vectors[:,1:2], eig_vectors[:,2:3]))