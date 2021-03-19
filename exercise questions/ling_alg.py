#%%

import math
import numpy as np

arr = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])

arrlist = [arr] * 100

# arrlist
# %%

print(np.dot(arr, arr))
# %%

from functools import reduce

print(reduce(lambda mul, x: np.dot(x, mul), arrlist))
# %%
