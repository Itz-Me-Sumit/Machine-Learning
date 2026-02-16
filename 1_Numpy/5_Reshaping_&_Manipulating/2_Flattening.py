"""

    arr.ravel() -> it'will modify the original array 

    arr.flatten() -> it'll first take a copy of original array and then modify, it'll not modify original array.

"""

import numpy as np
arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(arr.ravel())
print(arr.flatten())