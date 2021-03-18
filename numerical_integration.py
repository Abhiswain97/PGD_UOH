# %%
import math

# %%
def f(x):
    return math.sin(x) / x


# Integrate f(x) from -10 to 10

f(10)
# %%
x = -10
area = 0
delta = 0.1

while x <= 10:

    if x == 0:  # avoid the nan case when x = 0 for sin(x)/x
        continue

    area += f(x) * delta
    x += delta

print(f"area = {area}")


#%%

# Improve using trapezoidal rule
x = -10
area = 0
delta = 0.1

while x <= 10:

    if x == 0:  # avoid the nan case when x = 0 for sin(x)/x
        continue

    area += (f(x) + f(x + delta)) * (1 / 2) * delta
    x += delta

print(f"area = {area}")
