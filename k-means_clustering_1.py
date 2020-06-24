#추가 기능으로 사용하면 좋을 것 같아요.
#https://365datascience.com/pca-k-means/

from collections import defaultdict #나중에 제거
from random import uniform
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
from player_1 import Player, Record_Hitter, Record_Pitcher
import csv


#make list of players19
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

X =[[player.record[i].AVG] for i in range(len(player.record) - 1) for player in player_list]


#k-means clustering
def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2
    
    Returns a new point which is the center of all the points.
    """
    dimensions = points[0]

    new_center = []

    for dimension in range(len(dimensions)):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += p[dimension]

        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.
    """
    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)    
    for points in new_means.values():
        #print(points)
        centers.append(point_avg(points))

    return centers


def assign_points(data_points, centers):
    """
    Given a data set and a list of points betweeen other points,
    assign each point to an index that corresponds to the index
    of the center point on it's proximity to that point. 
    Return a an array of indexes of centers that correspond to
    an index in the data set; that is, if there are N points
    in `data_set` the list we return will have N elements. Also
    If there are Y points in `centers` there will be Y unique
    possible values within the returned list.
    """
    assignments = []
    for point in data_points:
        shortest = 10000  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    """
    dimensions = len(a)
    
    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)


def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]
            
            rand_point.append(uniform(min_val, max_val))

        centers.append(rand_point)

    return centers


def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    return zip(assignments, dataset)

Player_kmeans = k_means(X, 3)
Player_kmeans = list(Player_kmeans)
k_values = []
player_values = []
for i, j in Player_kmeans:
    k_values.append(i)
    player_values.append(j)

fig=plt.figure(figsize=(5,5))
axis = fig.add_subplot(111)
axis.set_title('k-means clustering with AVG of KBO players in 2019')
axis.grid(True)

plt.scatter(k_values, player_values, c = k_values, edgecolor = 'none', s=100)
plt.show()