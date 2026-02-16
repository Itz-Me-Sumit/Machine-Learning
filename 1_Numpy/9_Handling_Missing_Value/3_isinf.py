"""
    check wheather a array contains infinity(undefine) element
        np.isinf(array)
"""

import numpy as np
arr=np.array([1,2,np.inf,33,-np.inf ,88])
print(np.isinf(arr))

cleared_array=np.nan_to_num(arr,posinf=100 , neginf=-100)
print(cleared_array)