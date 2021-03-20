#%%

import math


def f(x):
    if x != 0:
        return math.sin(x) / x
    else:
        return math.nan


#%%
def slope_f(x, delta=0.001):
    return (f(x + delta) - f(x)) / delta


# %%

# Find maxima in range -2, 2
import random

# init
x_l = -2
x_u = +2
x = (x_u + x_l) / 2

# iterate
while True:  # Alwasys TRUE

    if math.isnan(
        slope_f(x, delta=0.001)
    ):  # Fix NAN case with random pertubation of x.
        x = x + random.random() / 100

    if (
        abs(slope_f(x, delta=0.001)) < 0.0001
    ):  # BREAK condition NOTE the less-than. [COMMON MISTAKE: >]
        break

    x = (x_u + x_l) / 2
    # middle point
    if slope_f(x, delta=0.001) > 0:  # adjust x_l
        x_l = x
    else:  # adjust x_u
        x_u = x

    print(slope_f(x, delta=0.001), x_l, x_u)

print("x:" + str(x) + "\t slope_f(x, delta=0.001): " + str(slope_f(x, delta=0.001)))


# %%
