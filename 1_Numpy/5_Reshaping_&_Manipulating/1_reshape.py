"""

    reshape : it used to reshape the array into new shape
              like we can reshape an array into 3 rows and 4 columns
              and even can reshape that same array into 2 rows and 6 column

    syntax : arr.reshape(row , column)

    -- can be reshaped only if dimentions matched.

"""

import numpy as np

arr=np.array([44,32,52,11,63,22,16,9,45,113,13,49])
reshape_arr=arr.reshape(3,4)
print(reshape_arr)
