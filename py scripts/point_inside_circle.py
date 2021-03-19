import math


def isInside(x, y, cx, cy, r):
    return True if math.sqrt(math.pow(cx - x, 2) + math.pow(cy - y, 2)) > r else False


if __name__ == "__main__":
    print(isInside(10, 12, 0, 0, 5))