from pprint import pprint


def subsetSumDP(arr, n, s):
    dp = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for j in range(s + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        print(f"\n State table after iteration {i}: \n")
        pprint(dp)

    return dp[n][s]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    s = 9
    res = subsetSumDP(arr, len(arr), s)
    print(f"There is a subset with {s}") if res else print("No subset found!")
