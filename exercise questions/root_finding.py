#%%

# Find a real valued "x" such that x^5 - x^4 + 2*x^3 - x^2 + x = 3

import math


def f(x):
    return x ** 5 - x ** 4 + 2 * x ** 3 - (2 * x) + x - 3


# %%

# plot the function

import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(-5, 5, 100)

plt.plot(a, f(a))
plt.grid()
plt.show()

# %%

# Fix this!


def bisection():

    xl, xu = -5, 5

    mid = (xl + xu) / 2

    while abs(f(mid)) > 0.001:

        mid = (xl + xu) / 2

        if f(mid) > 0:
            xl = mid
        else:
            xu = mid

        print(f(mid), xl, xu)

    print(f"Root at {mid} and f(x) = {f(mid)}")


# bisection()

#%%


def derivative_f(x):
    return (5 * x ** 4) - (4 * x ** 3) + (6 * x ** 2) - 1


# %%

"""
Algorithm:
Input: initial x, func(x), derivFunc(x)
Output: Root of Func()

Compute values of func(x) and derivFunc(x) for given initial x
Compute h: h = func(x) / derivFunc(x)
While h is greater than allowed error ε
    h = func(x) / derivFunc(x)
    x = x – h
"""

epsilon = 0.01


def newton_raphson_(x):
    h = f(x) / derivative_f(x)
    c = 0
    while abs(h) >= epsilon:
        c += 1
        h = f(x) / derivative_f(x)
        x = x - h

    print(f"The value of the root is : {x}")
    print(f"Iterations: {c}")

    return x


x = -2

print(f"{newton_raphson_(x):.5f}")

# %%
f(1.22852)
# %%
