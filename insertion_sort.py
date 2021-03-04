from typing import List


def printList(arr: List):
    for i in arr:
        print(i, end=" ")


def insertionSort(arr: List):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    a = [6, 5, 3, 1, 8, 7, 2, 4]
    print(a)

    insertionSort(a)
    printList(a)