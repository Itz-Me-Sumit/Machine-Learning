"""
    combining arrays
      - vertically
      - horizontally
    
      vstack() = row wise
      hstack() = column wise

"""

import numpy as np

arr1=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
arr2=np.array([[3,2,7],
               [8,1,0],
               [3,0,5]])

vertically=np.vstack((arr1,arr2))
print(vertically)

horizontally=np.hstack((arr1,arr2))
print(horizontally)