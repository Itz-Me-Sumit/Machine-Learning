import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

flatten_insertion=np.insert(arr,1,[4,7,0],axis=None)
print(flatten_insertion)

print()

row_insertion=np.insert(arr,1,[4,7,0],axis=0)
print(row_insertion)

print()

col_insertion=np.insert(arr,1,[4,7,0],axis=1)
print(col_insertion)