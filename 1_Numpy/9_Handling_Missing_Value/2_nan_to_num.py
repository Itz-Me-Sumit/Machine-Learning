"""
    if we want to replace nan(nothing) to any value

        np.nan_to_num(array , nan=value)
            - default : nan = 0

"""

import numpy as np
arr=np.array([12,45,np.nan,0,np.nan,88])
print(np.nan_to_num(arr , nan=100)) 