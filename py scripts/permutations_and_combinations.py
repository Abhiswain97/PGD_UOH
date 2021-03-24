# %%

# Using library functions

from itertools import permutations, combinations

arr = [1, 2, 3]

print(list(combinations(arr, r=2)))
print(list(permutations(arr, r=2)))

# %%

# from scratch using recursion


def permutations(arr):
    if len(arr) == 1:
        return [arr]

    reslist = []
    for i in arr:

        rem = [x for x in arr if x != i]

        z = permutations(rem)

        for j in z:
            reslist.append([i] + j)

    return reslist


# %%

permutations(arr)
# %%


def combinations(arr):

    reslist = []
    for a in arr:
        z = combinations(arr)
        print(z)

    for i in z:
        reslist.append(i)

    return reslist


# %%

combinations(arr)
# %%
