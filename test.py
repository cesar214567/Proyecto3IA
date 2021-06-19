import numpy as np

set1 = [1,2,3,4,5]
set2 = [2,3,4,5,6]

print(np.mean( np.array([ set1, set2 ]), axis=0 ))