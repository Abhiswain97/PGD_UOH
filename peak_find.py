from scipy.signal import find_peaks


def find_peak(arr: list):
    if len(arr) == 1:
        return 0
    if arr[0] >= arr[1]:
        print(0)
    if arr[len(arr) - 1] >= arr[len(arr) - 2]:
        print(len(arr) - 1)
    for i in range(1, len(arr) - 1):
        if arr[i] >= arr[i + 1] and arr[i - 1] <= arr[i]:
            return i


if __name__ == "__main__":
    arr = [41, 3, 20, 4, 1, 24]

    print(find_peak(arr))

    peaks, _ = find_peaks(arr, height=[2, 41])

    print(peaks)