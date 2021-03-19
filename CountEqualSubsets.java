package com.company.DP;

public class CountEqualSubsets {
    static boolean[][] T;
    static int[][] memo;

    static void printMatrix(int n, int sum, int iteration){
        System.out.println("State Table after iteration " + iteration + ": ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < sum/2; j++) {
                System.out.print(" " + T[i][j]);
            }
            System.out.println();

            }
    }

    static int countEqualSumSubset(int[] arr, int n, int sum){
        int count = 0;
        if (sum % 2 != 0) return count;
        else {
            T = new boolean[n+1][sum/2+1];

            for (int i = 0; i < n; i++) {
                T[i][0] = true;
            }
            for (int j = 1; j < sum/2; j++) {
                T[0][j] = false;
            }
            printMatrix(n, sum, 0);
            for (int i = 1; i < n; i++) {
                for (int j = 0; j < sum/2; j++) {
                    if (arr[i-1] > j) T[i][j] = T[i-1][j];
                    else if (arr[i-1] == j) {
                        T[i][j] = true;
                        count = count + 1;
                    }
                    else T[i][j] = T[i-1][j] || T[i-1][j - arr[i-1]];
                }
                printMatrix(n, sum, i);
            }
        }

        return count;
    }


    public static void main(String[] args) {
        int[] arr = { 1, 5, 5, 11 };
        int n = arr.length;
        int sum = 0;
        for (int j : arr) {
            sum += j;
        }
        // Function call

        System.out.println("No of equal subsets: " + countEqualSumSubset(arr, n, sum));
//        System.out.println("No of equal subsets: " + memoizedCountEqualSumSubset(arr, n, sum));
    }
}
