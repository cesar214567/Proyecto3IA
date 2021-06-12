import numpy as np
import math
from random import random, randrange
from PIL import Image
import random
from scipy import spatial
import matplotlib.pyplot as plt
import csv 
import sys

nodes=[]
points = []
with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        points.append((int(row[0]),int(row[1])))

def dist(a, b):
    return math.dist(a,b)
    
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
    def __init__(self,x,r=1):
        self.number = x
        self.items = []
        self.r = r
        self.itemCount = 0

    def build_cluster(self,node):
        global tree
        self.items.append(node)
        self.itemCount += 1
        node.cluster = self.number
        neighbours = node.getItems(self.r)
        for neigh in neighbours:
            if neigh.cluster == -1:
                # print("HERE - ", neigh.point)
                self.build_cluster(neigh)

    def isValid(self):
        return self.itemCount >= 2

    def define(self, node):
        self.build_cluster(node)
        if(not self.isValid()):
            for i in range(len(self.items)-1, -1, -1):
                self.items[i].cluster = -2
                self.items.pop()
            return False
        return True


for point in points: 
    nodes.append(Node(point))


tree =spatial.KDTree(points)

clusters = []
size = len(nodes)

r = 1 

cluster_num = 0
for node in nodes:
    if node.cluster == -1:
        new_cluster = Cluster(cluster_num)
        if(new_cluster.define(node)):
            clusters.append(new_cluster)
            cluster_num += 1
print("asdas: ")

for x in clusters:
    print(x.items)
    print("------------")
print("cluster_num: " + str(cluster_num))