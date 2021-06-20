import numpy as np
import math
import matplotlib.pyplot as mp
from random import random, randrange
from PIL import Image
import random
from scipy.spatial import distance


class Node:
    def __init__(self,tupla,name):
        self.name = name
        self.point = tupla
        self.cluster = 0
        self.dimensions = len(self.point)
        

class Cluster:
    def __init__(self,tupla):
        self.point = list(tupla)
        self.items = []
    def moveCenter(self):
        tempnode = self.items[0]
        for dimension in range(tempnode.dimensions):
            average = 0
            for node in self.items:
                if(isinstance(node, Node)):
                    average += node.point[dimension]
            average = average/len(self.items)
            self.point[dimension] = average

def dist(a, b):
    return distance.euclidean(a,b)

def get_nearests(nodes,clusters):
    for node in nodes:
        minimum = dist(node.point, clusters[0].point)
        node.cluster = 0
        for i in range(len(clusters)):
            distance = dist(node.point, clusters[i].point)
            if (distance < minimum):
                minimum = distance
                node.cluster = i
            clusters[node.cluster].items.append(node)

def while_loop(nodes, clusters,iters=None):
    if (iters==None):
        return clusters
    else:
        for i in range(iters):
            get_nearests(nodes,clusters)
            for cluster in clusters:
                cluster.moveCenter()
                cluster.items.clear()


def RepeatedColor(nodeTemp,clusters):
    print("#######")
    print(nodeTemp[2:])
    for cluster in clusters:
        print(cluster.point[2:])
        print(dist(cluster.point[2:],nodeTemp[2:]))
        print("----")
        if(dist(cluster.point[2:],nodeTemp[2:])<10):
            return True
    return False




def KMeans(points):
    #Get clase names
    file = open("clase.csv")
    lista = []
    for line in file: 
        l = line.split(",")
        lista.append(l[1])
    lista = lista[1:]
    new_lista = list(dict.fromkeys(lista))

    nodes=[]
    i = 0
    for point in points:
        name = lista[i]
        nodes.append(Node(point,name))
        i+=1

    clusters = []
    size = len(nodes)
    K = 7
    for i in range(K):
        nodeTemp = nodes[random.randint(0,size)].point        
        clusters.append(Cluster(nodeTemp))
    for i in clusters:
        print(i.point)
    while_loop(nodes,clusters,15)
    get_nearests(nodes,clusters)
    returning_points=[]
    for cluster in clusters:
        list_clust = []
        for node in cluster.items:
            returning_points.append(node.point)
            
  
    #im.show()

    #im.show()


    return returning_points
    
    
    
  
read_db()