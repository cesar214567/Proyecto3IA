import numpy as np
import math
from random import random, randrange
from scipy.spatial import distance
import matplotlib.pyplot as plt
import csv 




def dist(a, b):
    return distance.euclidean(a,b)
    
class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = -1
        self.dimensions = len(self.point)

    def getItems(self,r):
        global tree
        temp = []
        data = tree.query_ball_point(self.point,r)
        # print(data)
        for item in data:
            # print(nodes[item].point)
            temp.append(nodes[item])
        return temp

class Cluster:
    def __init__(self,x):
        self.number = x
        self.visited = False
        self.items = []
        self.items2 = []
        self.itemCount = 0

    def build_cluster(self,node):
        global tree
        self.items.append(node)
        self.itemCount += 1
        node.cluster = self.number
        while (len(self.items)!=0):
            node_temp = self.items[0]
            self.items.pop(0)
            self.items2.append(node_temp)
            #print(node_temp.point)
            neighbours = node_temp.getItems(self.r)
            for neigh in neighbours:
                if neigh.cluster == -1:
                    # print("HERE - ", neigh.point)
                    self.items.append(neigh)
                    self.itemCount+=1
                    neigh.cluster=self.number
        
    def isValid(self):
        return self.itemCount >= 25

    def define(self, node):
        self.build_cluster(node)
        if(not self.isValid()):
            for i in range(len(self.items2)):
                self.items2[i].cluster = -1
            self.itemCount=0 
            self.items2 = []
            return False
        return True

def algorithm():
    nodes = []
    clusters = []
    for i in range(10):
        sub_data =[]
        for i in range(3):
            sub_data.append(random.uniform(0,10))
        node = Node(sub_data)
        nodes.append(node)
        clusters.append(Cluster(node)) 
    
    size = len(nodes)

    cluster_num = 0
    while(len(clusters) > 1):
        cont = 1
        for cluster in clusters:
            if not cluster.visited:
                cluster.visited = True
                nearest_cluster = 0
                min_dist = 0
                for target in clusters:
                    if (target == cluster):
                        continue 
                    temp = dist(cluster, target)
                    if (temp < min_dist):
                        min_dist = temp
                        nearest_cluster = target
                
                new_cluster = Cluster(cluster_num)
                if(new_cluster.define(node)):
                    clusters.append(new_cluster)
                    cluster_num += 1
                #else:
                    #print(new_cluster.items2)
        #print("asdas: ")

    for temp in clusters:
        
        x=[]
        y=[]
        print(temp.itemCount)
        for item in temp.items2:
            x.append(item.point[0])
            y.append(item.point[1])
        plt.plot(x,y,'*')
    plt.show()
    print("cluster_num: " + str(cluster_num))

    
