#%%
import math

cx1, cy1, cr1 = list(map(float, input().split()))
# %%

cx2, cy2, cr2 = list(map(float, input().split()))

# %%


def center_distance(cx1, cy1, cx2, cy2):
    return math.sqrt(math.pow(cx1 - cy1, 2) + math.pow(cx2 - cy2, 2))


def isIntersecting(cr1, cr2):
    if center_distance(cx1, cy1, cx2, cy2) == (cr1 + cr2):
        print("Intersecting at one point only")
    else:
        print("Intersecting at more than one point")


isIntersecting(cr1, cr2)
# %%
