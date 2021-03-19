package com.company.DP;

public class MinSubsetDifference {

    static boolean[][] T;

    static void printMatrix(int n, int sum, int iteration){

        System.out.println("State Table after iteration " + iteration + ": ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < sum/2; j++) {
                System.out.print(" " + T[i][j]);
            }
            System.out.println();
        }
    }

    static int minSubsetDiff(int[] arr, int n, int sum){

        T = new boolean[n+1][sum/2+1];

        // Initialize
        for (int i = 0; i < n; i++) {
            T[i][0] = true;
        }
        for (int j = 1; j < sum/2; j++) {
            T[0][j] = false;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < sum/2; j++) {
                if (arr[i-1] > j) T[i][j] = T[i-1][j];
                else T[i][j] = T[i-1][j] || T[i-1][j - arr[i-1]];
            }
            printMatrix(n, sum, i);
        }

        int diff = Integer.MAX_VALUE;
        for (int i = 0; i < sum/2; i++) {
            int second = sum/2 - i;
            if (T[n-1][i] && diff > Math.abs(i - second)) {
                diff = Math.abs(i - second);
                System.out.println(diff);
            }
        }
        return diff;
    }

    public static void main(String[] args) {
        int[] arr = {2, 4, 2, 3};
        int n = arr.length;
        int sum = 0;
        for (int j : arr) {
            sum += j;
        }

        System.out.print("The minimum difference"+
                " between two sets is " +
                minSubsetDiff(arr, n, sum));
    }
}
