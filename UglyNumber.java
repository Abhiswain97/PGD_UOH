package com.company.DP;

import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

public class UglyNumber {

    static boolean isUgly(int n){

        if (n < 1) return false;
        while (n % 2 == 0) n /= 2;
        while (n % 3 == 0) n /= 3;
        while (n % 5 == 0) n /= 5;

        return n == 1;
    }

    static int nthUglyNumer(int n){
        int count = 2, i = 0;
        while (count < n){
            if (isUgly(i)) {
                count++;
            }
            i++;
        }
        return i;
    }

    static int nthUglyNumberDP(int n){
        int[] ugly = new int[n];  // To store ugly numbers
        int i2 = 0, i3 = 0, i5 = 0;
        int next_multiple_of_2 = 2;
        AtomicInteger next_multiple_of_3 = new AtomicInteger(3);
        int next_multiple_of_5 = 5;
        int next_ugly_no = 1;

        ugly[0] = 1;

        for(int i = 1; i < n; i++)
        {
            next_ugly_no = Math.min(next_multiple_of_2,
                    Math.min(next_multiple_of_3.get(),
                            next_multiple_of_5));

            ugly[i] = next_ugly_no;
            if (next_ugly_no == next_multiple_of_2)
            {
                i2 = i2+1;
                next_multiple_of_2 = ugly[i2]*2;
            }
            if (next_ugly_no == next_multiple_of_3.get())
            {
                i3 = i3+1;
                next_multiple_of_3.set(ugly[i3] * 3);
            }
            if (next_ugly_no == next_multiple_of_5)
            {
                i5 = i5+1;
                next_multiple_of_5 = ugly[i5]*5;
            }
        } /*End of for loop (i=1; i<n; i++) */
        return ugly[n - 2];
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter value of n: ");
        int n = sc.nextInt();
        System.out.printf("%dth Ugly number using brute-force is: %d\n", n, nthUglyNumer(n));
        System.out.printf("%dth Ugly number using DP is: %d\n", n, nthUglyNumberDP(n));
    }
}
