"""
    if we want to detect is any value missing in array.
"""

import numpy as np
arr=np.array([1,2,np.nan,3,6,np.nan,0,8])
print(np.isnan(arr))