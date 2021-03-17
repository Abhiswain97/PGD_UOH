from itertools import permutations, combinations

arr = [1, 2, 3]

print(list(combinations(arr, r=2)))
print(list(permutations(arr, r=2)))