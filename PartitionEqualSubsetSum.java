package com.company.DP;

public class PartitionEqualSubsetSum {

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

    static boolean partitionEqualSumSubset(int[] arr, int n, int sum){
        if (sum % 2 != 0) return false;
        else {
            T = new boolean[n+1][sum/2+1];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < sum/2; j++) {
                    if (i == 0 || j == 0) T[i][j] = false;
                    else if (arr[i-1] > j) T[i][j] = T[i-1][j];
                    else if (arr[i-1] == j) T[i][j] = true;
                    else T[i][j] = T[i-1][j] || T[i-1][j - arr[i-1]];
                }
                printMatrix(n, sum, i);
            }
        }

        return T[n -1][sum/2 - 1];
    }


    public static void main(String[] args) {
        int[] arr = { 1, 5, 5, 11 };
        int n = arr.length;
        int sum = 0;
        for (int j : arr) {
            sum += j;
        }
        // Function call

        if (partitionEqualSumSubset(arr, n, sum)){
            System.out.println("Result: ");
            System.out.println("Can be divided into two "
                    + "subsets of equal sum");
        }

        else {
            System.out.println("Result: ");
            System.out.println(
                    "Can not be divided into "
                            + "two subsets of equal sum");
        }
    }
}
