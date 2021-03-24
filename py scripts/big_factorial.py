def multiply(x, arr, size):
    carry = 0
    for i in range(size):
        p = arr[i] * x + carry
        arr[i] = p % 10
        carry = p // 10

    while carry > 0:
        arr[size] = carry % 10
        carry = carry // 10
        size += 1

    return size


if __name__ == "__main__":
    n = 5
    a = [1] * 1000
    size = 1
    for i in range(2, n + 1):
        size = multiply(i, a, size)

    print(list(reversed(a[:size])))
