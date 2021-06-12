import numpy as np
import math
import matplotlib.pyplot as plt
from random import random, randrange
from PIL import Image
import random
from scipy import spatial
#https://rtree.readthedocs.io/en/latest/install.html#nix
#https://libspatialindex.org/en/latest/#current-release-mit
#https://stackoverflow.com/questions/3493061/how-do-range-queries-work-in-pythons-kd-tree

def dist(a, b):
    return math.dist(a,b)    

class Node:
    def __init__(self,tupla):
        self.point = tupla
        self.cluster = 0
        self.dimensions = len(self.point)


class Cluster:
    def __init__(self,tupla,r):
        self.point = list(tupla)
        self.items = []
        self.r = r 
    def moveCenter(self):
        tempnode = self.items[0]
        for dimension in range(tempnode.dimensions):
            average = 0
            for node in self.items:
                if(isinstance(node, Node)):
                    average += node.point[dimension]
            average = average/len(self.items)
            self.point[dimension] = average

    def getItems(self,tree,nodes):
        data =tree.query_ball_point(self.point,self.r)
        self.items = [Node(nodes[item].point) for item in data]
        return self.items

    def recalc(self, iters,tree,nodes):
        print(self.point)
        for i in range(iters):
            self.getItems(tree,nodes)
            self.moveCenter()
        print(self.point)



def RepeatedColor(nodeTemp,clusters):
    print("#######")
    print(nodeTemp[2:])
    for cluster in clusters:
        print(cluster.point[2:])
        print(dist(cluster.point[2:],nodeTemp[2:]))
        print("----")
        if(dist(cluster.point[2:],nodeTemp[2:])<5):
            return True
    return False


def MeanShift(pix_val, num,filename,w,h):
    nodes=[]
    tree =spatial.KDTree(pix_val)
    for item in pix_val:
        nodes.append(Node(item))

    clusters = []
    size = len(nodes)
    K = 10
    r = 20
    for i in range(K):
        nodeTemp = nodes[random.randint(size*i/K,size*(i+1)/K)].point
        while(RepeatedColor(nodeTemp,clusters)):
            nodeTemp = nodes[random.randint(size*i/K,size*(i+1)/K)].point
        clusters.append(Cluster(nodeTemp,r))        
        #clusters.append(Cluster(nodes[random.randint(0,size)].point,r))
        #clusters.append(Cluster(nodes[random.randint(size*i/K,size*(i+1)/K)].point,r))

    for cluster in clusters:
        cluster.recalc(100,tree,nodes)

    fig, ax = plt.subplots()
    image = plt.imread(filename)
    ax.imshow(image,extent=[0,w,0,h])
    for temp in clusters:     
        x=[]
        y=[]
        for item in temp.items:
            x.append(item.point[0])
            y.append(item.point[1])
        plt.plot(x,y,'*')
    #print(xd)
    plt.show()
    plt.savefig("MEANSHIFT_"+str(num))
    plt.clf()

def read_db():
    i = 1
    file = open("files.txt","r")
    for line in file:
        #     if (i == 1):
        #         i += 1
        #         continue
        print(line)
        points = []
        im = Image.open(line[:-1], 'r')
        pix_val=list(im.getdata())
        #pix_val = im.convert("RGB")
        #pix_val=list([] im.getdata())
        pix_val = np.array(im)
        h,w = len(pix_val),len(pix_val[0])
        print(len(pix_val[0]))
        print(h,w)
        for y in range(h):
            for x in range(w):
                points.append((x*2.5, y*2.5, pix_val[y][x]/2))
        #print("----------------DBSCAN---------------")
        #DBSCAN(points, i)
        # print("----------------KMeans---------------")
        # KMeans(points,w,h)
        print("--------------Mean Shift-------------")
        MeanShift(points,i,line[:-1],w*2.5,h*2.5)
        points.clear()

read_db()