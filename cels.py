#from DBSCAN import DBSCAN
#from KMeans import KMeans
#from MeanShift import MeanShift
from PIL import Image
from scipy import misc
import numpy as np
import pandas


from numpy import mean
from numpy import std
from sklearn.decomposition import TruncatedSVD


def read_db():
    i = 1
    file = pandas.read_csv("dataset_tissue.csv")
    headers = list(file.columns)
    types = {}
    file2 = pandas.read_csv("clase.csv")
    for index, row in file2.iterrows():
        types[row['x']]=row['type']
    #print(types)
    index = 0 
    x = []
    for (colname,colval) in file.iteritems(): #colval.values = column values
        x.append(list(colval.values))
        #print(len(list(colval.values)))
    return x



def reduce_db(X,num):
    trun_svd =  TruncatedSVD(n_components = num)
    A_transformed = trun_svd.fit_transform(X)
   # print(A_transformed)
    return A_transformed
    


    
#lst = read_db()
#print(len(lst))
#reduce_db(lst,30)
#KMeans()