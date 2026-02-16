# astype :- it changes the datatype of elements in array.

import numpy as np
arr=np.array([12.3,44.2,33.33,90.0])

'''
    arr.astype(datatype)
'''

int_arr=arr.astype(int)
print(int_arr)


str_arr=arr.astype(str)
print(str_arr)