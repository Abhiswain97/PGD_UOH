import math


class Metrics:
    def __init__(self, v):
        self.v = v
        self.size = len(v)

    def mean(self):
        return sum(self.v) / self.size

    def median(self):
        self.v.sort()
        return (
            self.v[self.size // 2]
            if len(self.v) % 2 != 0
            else Metrics(
                [self.v[(self.size // 2) - 1], self.v[(self.size // 2)]]
            ).mean()
        )

    def variance(self):
        return (
            sum(list(map(lambda x: (x - Metrics(self.v).mean()) ** 2, self.v)))
            / self.size
        )

    def stdev(self):
        return math.sqrt(Metrics(self.v).variance())

    def mean_absolute_deviation(self):
        return Metrics(
            list(map(lambda x: abs(x - Metrics(self.v).median()), self.v))
        ).median()

    def nth_percentile(self, n):

        # More about it: https://en.wikipedia.org/wiki/Percentile#Second_variant,_%7F'%22%60UNIQ--postMath-0000004A-QINU%60%22'%7F

        self.v.sort()

        x = (n / 100 * (self.size - 1)) + 1

        ipart = math.floor(x)
        dpart = x % 1

        return self.v[ipart - 1] + dpart * (self.v[ipart] - self.v[ipart - 1])

    def IQR(self):
        return self.nth_percentile(75) - self.nth_percentile(25)


if __name__ == "__main__":

    a = list(range(1, 7))

    print(f"Mean: {Metrics(a).mean()}")

    print(f"Median: {Metrics(a).median()}")

    print(f"Variance: {Metrics(a).variance()}")

    print(f"Standard Deviation: {Metrics(a).stdev()}")

    print(f"Mean Absolute Deviation: {Metrics(a).mean_absolute_deviation()}")

    print(f"90th percentile: {Metrics(a).nth_percentile(90)}")

    print(f"99th percentile: {Metrics(a).nth_percentile(99)}")

    print(f"IQR: {Metrics(a).IQR()}")