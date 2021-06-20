#Importing required modules
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.datasets import make_classification

#Creating array 
A = np.array([[3,4,3],[1,2,3],[4,2,1]])
#X, y = make_classification(n_samples=189, n_features=22215, random_state=7)
#
##Fitting the SVD class
#trun_svd =  TruncatedSVD(n_components = 10000)
#A_transformed = trun_svd.fit_transform(X)
#
#
#
##Printing the transformed matrix
#print("Transformed Matrix:")
#print(A_transformed)

b = np.array([3,4,3])
print(b)
for line in A:
    print(line)
    if line.all()  == b.all():
        print("Si")
    else:
        print("No")
