import numpy as np
import math
from random import random, randrange
from PIL import Image
import random
from scipy import spatial
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv 
import sys
from cels import read_db
from cels import reduce_db


nodes=[]
points = []
def dist(a, b):
    print(math.dist(a,b))
    return math.dist(a,b)
    
class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = -1
        self.dimensions = len(self.point)

    def getItems(self,r, tree):
        global nodes
        temp = []
        data = tree.query_ball_point(self.point,r)
        # print(data)
        for item in data:
            # print(nodes[item].point)
            temp.append(nodes[item])
        return temp

class Cluster:
    def __init__(self,x,name,r=4,):
        self.number = x
        self.items = []
        self.items2 = []
        self.r = r
        self.itemCount = 0
        self.name = name

    def build_cluster(self,node, tree):
        self.items.append(node)
        self.itemCount += 1
        node.cluster = self.number
        while (len(self.items)!=0):
            node_temp = self.items[0]
            self.items.pop(0)
            self.items2.append(node_temp)
            #print(node_temp.point)
            neighbours = node_temp.getItems(self.r, tree)
            for neigh in neighbours:
                if neigh.cluster == -1:
                    # print("HERE - ", neigh.point)
                    self.items.append(neigh)
                    self.itemCount+=1
                    neigh.cluster=self.number
        
    def isValid(self):
        return self.itemCount >= 0

    def define(self, node, tree):
        self.build_cluster(node, tree)
        if(not self.isValid()):
            for i in range(len(self.items2)):
                self.items2[i].cluster = -1
            self.itemCount=0 
            self.items2 = []
            return False
        return True

def DBSCAN(points):
    #dic = {}
    #for i in range(0,len(points)):
    #    dic[points[i]] = i

    file = open("clase.csv")
    lista = []
    for line in file: 
        l = line.split(",")
        lista.append(l[1])
    lista = lista[1:]
    new_lista = list(dict.fromkeys(lista))


    print(len(points))
    for point in points: 
        nodes.append(Node(point))
    print("Info", len(points), len(points[0]), points[0])
    tree=[]
    tree =spatial.KDTree(points)

    clusters = []
    size = len(nodes)

    r = 60

    cluster_num = 0
    i = 0
    for node in nodes:
        if node.cluster == -1:
            new_cluster = Cluster(cluster_num,lista[i],r)
            if(new_cluster.define(node, tree)):
                clusters.append(new_cluster)
                cluster_num += 1
        i += 1
            #else:
                #print(new_cluster.items2)
    #print("asdas: ")
    
    for temp in clusters:     
        x=[]
        y=[]
        for item in temp.items2:
            x.append(item.point[0])
            y.append(item.point[1])

        print(temp.name[:-1])
        plt.plot(x,y,'*',label=temp.name[:-1])
        print("Cluster: %s, number %d" % (temp.name[:-1], len(temp.items2)))
    plt.legend()    
    plt.show()
    
    #plt.savefig("DBS_IMG_"+str(name))
    plt.clf()
    print("cluster_num: " + str(cluster_num))

    for c in new_lista:
        print("%s tiene %d"% (c,lista.count(c)))


lst = read_db()
new= reduce_db(lst,20)
DBSCAN(new)

