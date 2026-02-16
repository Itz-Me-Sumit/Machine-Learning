"""
    np.insert(array,index,value,axis=None)

        - array = original Array
        - index = where we want to insert value
        - value = value that we wanted to insert
        - axis = if " axis=None " -> insert in flatten shape
                    " axis=0 " -> insert row-wise
                    " axis=1 " -> insert column-wise

"""

import numpy as np

arr=np.array([44,32,52,11,63,22,16,9,45,113,13,49])
print(arr)

inserted_arr=np.insert(arr , 4 , 3232 , axis=0)
print(inserted_arr)