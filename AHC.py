import numpy as np
from random import random, randrange
from scipy.spatial import distance
import matplotlib.pyplot as plt


def dist(a, b):
    return distance.euclidean(a,b)
    
class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = -1
        self.dimensions = len(self.point)

    def print(self, numero):
        print("Node: ", numero, " - ", self.point)


class Cluster:
    def __init__(self,x):
        self.number = x
        self.visited = False
        self.items = []
        self.itemCount = 0
        self.point = []

    def build_cluster(self,clusters):
        temp = np.zeros(len(clusters[0].point))       
        for cluster in clusters:
            self.items.append(cluster)
            if(type(cluster)=='Cluster'):
                self.itemCount+=cluster.itemCount
            else:
                self.itemCount = 1
            temp += cluster.point
        self.point = temp
    
    def print(self, numero):
        temp = numero + " - " + str(self.number)
        print("cluster: ", temp)
        for i in self.items:
            i.print(temp)
    
    def print2(self):
        self.items[0].print()
        print(self.number)
        if(len(self.items) > 1):
            self.items[1].print()

def algorithm(matrix):
    nodes = []
    clusters = []
    index = 0
    for row in matrix:
        node = Node(row)
        nodes.append(node)
        temp = Cluster(index)
        #print(node)
        temp.build_cluster([node])
        clusters.append(temp)
        index+=1
    size = len(nodes)

    cluster_num = 10
    while(len(clusters) > 1):
        cont = 1
        cluster = clusters.pop(0)
        #for cluster in clusters:
            #if not cluster.visited:
        #cluster.visited = True
        nearest_cluster = clusters[0]
        min_dist = dist(cluster.point, clusters[0].point)
        for target in clusters:
            if (target == cluster):
                continue 
            temp = dist(cluster.point, target.point)  # preguntar al profe 
            if (temp < min_dist):
                min_dist = temp
                nearest_cluster = target
        
        new_cluster = Cluster(cluster_num)  #,np.mean( np.array([ cluster.point, nearest_cluster.point ]), axis=0 )
        new_cluster.build_cluster([cluster, nearest_cluster])
        clusters.remove(nearest_cluster)
        clusters.append(new_cluster)
        cluster_num += 1
    clusters[0].print("init")

matrix= [
    [2],
    [1],
    [4],
    [3],
    [5],
    [9],
    [8],
    [7],
    [10],
    [6]
]

algorithm(matrix)