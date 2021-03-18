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

    area += f(x) * delta
    x += delta

print(f"area = {area}")