package com.company.DP;

import java.util.HashMap;

public class Fibonacci {

    static HashMap<Integer, Integer> fib = new HashMap<>();

    static int naiveRecursiveFib(int n){
        if (n <= 2) return 1;
        else return naiveRecursiveFib(n-1) + naiveRecursiveFib(n-2);
    }

    static int memoizedRecursiveFib(int n){
        int f;

        if (fib.containsKey(n)) return fib.get(n);
        else{
            if (n <= 2) f = 1;
            else f = memoizedRecursiveFib(n-1) + memoizedRecursiveFib(n-2);
        }

        fib.put(n, f);
        return fib.get(n);

    }

    static int bottomUpifyFib(int n){
        int[] fibArr = new int[n+1];
        fibArr[0] = 0;
        fibArr[1] = 1;
        for (int i = 2; i <= n; i++) {
            fibArr[i] = fibArr[i -1] + fibArr[i-2];
        }
        return fibArr[n];
    }

    static void calculateTime(String Fname, int n){
        long start = System.currentTimeMillis();

        if (Fname.equals("naiveRecursiveFib")) System.out.println(naiveRecursiveFib(n));
        if (Fname.equals("memoizedRecursiveFib")) System.out.println(memoizedRecursiveFib(n));
        if (Fname.equals("bottomUpifyFib")) System.out.println(bottomUpifyFib(n));

        long end = System.currentTimeMillis();

        System.out.println("Time taken by " + Fname + ": " + (end - start) + " ms");
    }

    public static void main(String[] args) {

        calculateTime("memoizedRecursiveFib", 45);
        calculateTime("bottomUpifyFib", 45);
        calculateTime("naiveRecursiveFib", 45);

    }
}
