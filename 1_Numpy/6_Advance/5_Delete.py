

import numpy as np

arr=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

flatten_array_delete=np.delete(arr , 1 , axis=None)
    # it will first flat the array and then delete element at that index
print(flatten_array_delete)

row_wise_delete=np.delete(arr,1,axis=0)
    # it will delete 2nd row (index=1)
print(row_wise_delete)

col_wise_delete=np.delete(arr,1,axis=1)
    # it will delete 2nd column (index=1) 
print(col_wise_delete)