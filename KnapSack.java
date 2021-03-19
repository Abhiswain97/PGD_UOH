package com.company.DP;

import java.util.Arrays;

public class KnapSack {

    static int[][] memo;

    static void printMatrix(int n, int sum, int iteration){
        System.out.println("State Table after iteration " + iteration + ": ");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < sum; j++) {
                System.out.print(" " + memo[i][j]);
            }
            System.out.println();
        }
    }

    static int naiveRecursiveKnapSack(int[] wt, int[] val, int W, int n){
        if (W == 0 || n == 0) return 0;
        if(wt[n-1] > W) return naiveRecursiveKnapSack(wt, val, W, n - 1);
        else return Math.max(val[n - 1] + naiveRecursiveKnapSack(wt, val, W - wt[n - 1], n - 1),
                    naiveRecursiveKnapSack(wt, val, W, n - 1));
    }

    static int memoizedKnapSack(int[] wt, int[] val, int W, int n){
        if (W == 0 || n == 0) return 0;
        if (memo[n][W] != -1) return memo[n][W];
        if (wt[n] <= W){
            memo[n][W] = Math.max(
                    val[n - 1] + memoizedKnapSack(wt, val, W - wt[n - 1], n - 1),
                    memoizedKnapSack(wt, val, W, n - 1)
            );
            printMatrix(n, W, 0);
        }
        memo[n][W] = memoizedKnapSack(wt, val, W, n - 1);
        printMatrix(n, W, 0);

        return memo[n][W];
    }

    static int bottomUpifyKnapSack(int[] wt, int[] val, int W, int n){
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= W; j++) {
                if (i == 0 || j == 0) memo[i][j] = 0;
                else if(wt[i-1] > j) memo[i][j] = memo[i-1][j];
                else memo[i][j] = Math.max(memo[i-1][j], val[i-1] + memo[i-1][j-val[i-1]]);
            }
        }
        return memo[n][W];
    }

    public static void main(String[] args) {
        int[] wt = {1,2,3};
        int[] val = {2,3,5};
        int n = wt.length;
        int W = 5;

        memo = new int[n+1][W+1];
        for (int i = 0; i < n; i++) {
            Arrays.fill(memo[i], -1);
        }
        printMatrix(n, W, 0);
        System.out.println(naiveRecursiveKnapSack(wt, val, W, n));
        System.out.println(memoizedKnapSack(wt, val, W, n));
        System.out.println(bottomUpifyKnapSack(wt, val, W, n));

    }
}

