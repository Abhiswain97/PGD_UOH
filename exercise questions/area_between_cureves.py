#%%

import math
import numpy as np
import matplotlib.pyplot as plt

#%%


def f1(x):
    return np.exp(x)


def f2(x):
    return x ** 3


def newFunc(x):
    return abs(f1(x) - f2(x))


#%%

x = np.linspace(0, 4)

plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.grid(True)
plt.show()


# %%

x = 0
area = 0
delta = 0.0001

while x <= 4:

    area += (newFunc(x) + newFunc(x + delta)) * (1 / 2) * delta

    x += delta

print(f"Aread between the curve is: {area}")
# %%
