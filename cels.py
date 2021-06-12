from DBSCAN import DBSCAN
#from KMeans import KMeans
#from MeanShift import MeanShift
from PIL import Image
from scipy import misc
import numpy as np
import pandas

def read_db():
    i = 1
    file = pandas.read_csv("dataset_tissue.csv")
    headers = list(file.columns)
    types = {}
    file2 = pandas.read_csv("clase.csv")
    for index, row in file2.iterrows():
        types[row['x']]=row['type']
    print(types)
    index =0 
    for (colname,colval) in file.iteritems(): #colval.values = column values
        #resize(colval.values)    
        continue

#read_db()