"""
    - we can contatenate two array about same axis(row,column)
    - syntax :
        np.concatenate( (array1,array2) , axis = (0,1))
            axis=0 -> row-wise
            axis=1 -> column-wise

"""


import numpy as np

arr1=np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

arr2=np.array([[0,2,5],
               [6,3,9],
               [5,1,7]])

flatten_arr=np.concatenate( (arr1 , arr2) , axis=None )
print(flatten_arr)
"""
    output : [1 2 3 4 5 6 7 8 9 0 2 5 6 3 9 5 1 7]
"""


row_wise_concatenate=np.concatenate( (arr1 , arr2) , axis=0 )
print(row_wise_concatenate)
"""
    output : [[1 2 3]
              [4 5 6]
              [7 8 9]
              [0 2 5]
              [6 3 9]
              [5 1 7]]
"""

col_wise_concatenate=np.concatenate( (arr1 , arr2) , axis=1 )
print(col_wise_concatenate)
"""
    output : [[1 2 3 0 2 5]
              [4 5 6 6 3 9]
              [7 8 9 5 1 7]]
"""
