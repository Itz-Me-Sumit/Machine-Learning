"""
    np.split(array , numbers of parts) :- split into equal parts
    np.hsplit() :- split vertically
    np.vsplit() :- split horizontally

"""

import numpy as np

arr=np.array([1,2,3,4,5,6])

arr1=np.array([[1,2,3],
               [4,5,6],])

arr2=np.array([[3,2,7],
               [8,1,0],])

print()

print(np.split(arr , 3))
print()

print(np.hsplit(arr1 , 3))
print()

print(np.vsplit(arr2 , 2))