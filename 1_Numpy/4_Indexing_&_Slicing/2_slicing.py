"""
    array[start:stop:step]

"""

import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13])

print(arr[2:8])  #arr[start:stop]
print(arr[2:13:3]) #arr[start:stop:step]
print(arr[:8])
print(arr[4:])
print(arr[:])
print(arr[::-1])