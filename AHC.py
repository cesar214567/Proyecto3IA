import numpy as np
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
        self.data = {}

    def build_cluster(self,clusters,name=None):
        temp = np.zeros(len(clusters[0].point))       
        for cluster in clusters:
            self.items.append(cluster)
            if(len(clusters)>1):
                self.itemCount+=cluster.itemCount
                temp += cluster.point*cluster.itemCount
                for key in cluster.data.keys():
                    if key in self.data.keys():
                        self.data[key]+=cluster.data[key]
                    else:
                        self.data[key]=cluster.data[key]
            else:
                self.itemCount = 1
                temp += cluster.point
                self.data[name]=1
        self.point = temp/self.itemCount
    
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

    file = open("clase.csv")
    lista = []
    for line in file: 
        l = line.split(",")
        lista.append(l[1])
    lista = lista[1:]
    nodes = []
    clusters = []
    index = 0

    for row in matrix:
        node = Node(row)
        nodes.append(node)
        temp = Cluster(index)
        #print(node)
        temp.build_cluster([node],lista[index])
        clusters.append(temp)
        index+=1
    size = len(nodes)
    K= 12
    cluster_num = len(matrix)
    while(len(clusters) > K):
        cluster = clusters.pop(0)
        nearest_cluster = clusters[0]
        min_dist = dist(cluster.point, clusters[0].point)
        for target in clusters:
            
            temp = dist(cluster.point, target.point)  # preguntar al profe 
            if (temp < min_dist):
                min_dist = temp
                nearest_cluster = target
        new_cluster = Cluster(cluster_num)  
        new_cluster.build_cluster([cluster, nearest_cluster])
        
        clusters.remove(nearest_cluster)
        clusters.append(new_cluster)
        cluster_num += 1
    #print('----------------------------')
    #clusters[0].print("init")
    for cluster in clusters:
        print(cluster.data)


#algorithm(matrix)