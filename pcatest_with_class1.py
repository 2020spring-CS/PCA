import numpy as np
import matplotlib.pyplot as plt

from player_1 import Player
import csv

#make list of players19
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

f.close()

#code from pca_1.ipynb
X = []
for player in player19_list:
    stat = [player.AVG, player.XBH, player.GO, player.AO, player.GW_RBI, player.BB_K, player.P_PA, player.ISOP, player.XR, player.GPA]
    X.append(stat)

X_std= (X-np.mean(X, axis=0))/ np.std(X, axis=0)
mean_vec= np.mean(X_std, axis=0)
cov_mat=(X_std-mean_vec).T.dot((X_std-mean_vec))/(X_std.shape[0]-1)
cov_mat=np.cov(X_std.T)
eig_vals, eig_vectors = np.linalg.eig(cov_mat)

idx= np.argsort(eig_vals)[::-1]
a3= np.dot(X_std, eig_vectors[:,:3])
a2= np.dot(X_std, eig_vectors[:,:2])
a1= np.dot(X_std, eig_vectors[:,:1])

fig=plt.figure(figsize=(5,5))
axis = fig.add_subplot(111)
axis.set_title('2 component PCA')
axis.grid(True)

plt.scatter(a2[:,0], a2[:, 1])
plt.show()