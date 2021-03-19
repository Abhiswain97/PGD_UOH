package com.company.DP;

import java.util.Collections;

public class MaxMarks {
    static int naiveMaxMarks(int T, int[] marks, int[] times, int n) {
        if (T == 0 || n == 0)
            return 0;
        if (times[n - 1] > T)
            return naiveMaxMarks(T, marks, times, n - 1);
        else
            return Math.max(marks[n - 1] + naiveMaxMarks(T - times[n - 1], marks, times, n - 1),
                    naiveMaxMarks(T, marks, times, n - 1));
    }

    static void printDPTable(int[][] DP, int n, int T, int k) {

        System.out.println("DP table after iteration: " + k);
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= T; j++) {
                System.out.print("  " + DP[i][j]);
            }
            System.out.println();
        }
    }

    static int bottomUpifyMaxMarks(int T, int[] marks, int[] times, int n) {
        int[][] DP = new int[n + 1][T + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= T; j++) {
                if (i == 0 || j == 0)
                    DP[i][j] = 0;
                else if (times[i - 1] > j)
                    DP[i][j] = DP[i - 1][j];
                else
                    DP[i][j] = Math.max(DP[i - 1][j], marks[i - 1] + DP[i - 1][j - times[i - 1]]);
            }
            printDPTable(DP, n, T, i);
        }

        return DP[n][T];
    }

    public static void main(String[] args) {
        int[] marksarr = { 0, 6, 11, 2, 8 };
        int[] timearr = { 0, 4, 6, 2, 7 };

        System.out
                .println("Maximum marks that can be scored: " + naiveMaxMarks(10, marksarr, timearr, marksarr.length));
        System.out.println(
                "Maximum marks that can be scored: " + bottomUpifyMaxMarks(10, marksarr, timearr, marksarr.length));

        Collections.singletonList(marksarr).forEach(System.out::println);

    }
}
