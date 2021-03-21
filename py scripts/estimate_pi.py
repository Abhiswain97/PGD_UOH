#%%

import math
import random

# %%


def isInside(x, y, cx, cy, r):
    return True if math.sqrt(math.pow(cx - x, 2) + math.pow(cy - y, 2)) <= r else False


# %%

# Monte-Carlo simulation

cntInCircle = 0
n = 10000000

for i in range(n):
    x = random.random()
    y = random.random()

    if isInside(x, y, 0.5, 0.5, 0.5):
        cntInCircle += 1

print(cntInCircle / n * 4)
# %%
