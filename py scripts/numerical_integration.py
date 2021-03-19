# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
def f(x):
    return np.sin(x) / x


# Integrate f(x) from -10 to 10

f(10)

#%%

x = np.arange(-10, 10)

plt.plot(x, f(x))
plt.grid()
plt.show()


# %%
x = -10
area = 0
delta = 0.1

while x <= 10:
    print(x, area)
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
    print(x, area)

    if x == 0:  # avoid the nan case when x = 0 for sin(x)/x
        continue

    area += (f(x) + f(x + delta)) * (1 / 2) * delta
    x += delta

print(f"area = {area}")

# %%

# %%
