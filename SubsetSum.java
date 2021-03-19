package com.company.DP;

public class SubsetSum {

    static boolean[][] T;

    static void printMatrix(int n, int sum, int iteration) {

        System.out.println("State Table after iteration " + iteration + ": ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < sum; j++) {
                System.out.print(" " + T[i][j]);
            }
            System.out.println();
        }
    }

    static boolean naiveSubsetSum(int[] arr, int n, int sum) {
        // Base Cases
        if (n == 0)
            return false;
        if (sum == 0)
            return true;

        if (arr[n - 1] > sum)
            return naiveSubsetSum(arr, n - 1, sum);
        else
            return naiveSubsetSum(arr, n - 1, sum) || naiveSubsetSum(arr, n - 1, sum - arr[n - 1]);
    }

    // Time Complexity: O(n*sum) (pseudo-polynomial time)
    static boolean subsetSumDP(int[] arr, int n, int sum) {
        T = new boolean[n + 1][sum + 1];

        // Initialize
        for (int i = 0; i < n; i++) {
            T[i][0] = true;
        }
        for (int j = 1; j < sum; j++) {
            T[0][j] = false;
        }

        // Filling table in bottom-up fashion
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < sum; j++) {
                if (j < arr[i - 1])
                    T[i][j] = T[i - 1][j];
                if (j >= arr[i - 1])
                    T[i][j] = T[i - 1][j] || T[i - 1][j - arr[i - 1]];
            }
            printMatrix(n, sum, i);
        }

        return T[n - 1][sum - 1];

    }

    public static void main(String[] args) {
        int[] set = { 3, 34, 4, 12, 5, 2 };
        int sum = 9;
        int n = set.length;

        if (naiveSubsetSum(set, n, sum))
            System.out.println("Found a subset" + " with given sum");
        else
            System.out.println("No subset with" + " given sum");

        if (subsetSumDP(set, n, sum))
            System.out.println("Found a subset" + " with given sum");
        else
            System.out.println("No subset with" + " given sum");

    }
}
