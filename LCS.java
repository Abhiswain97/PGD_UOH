package Algorithms.Dynamic_Programming;

import java.util.Arrays;

/**
 * LCS
 */
public class LCS {

    static void Print(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");

            }
            System.out.println("\n");
        }
    }

    static int lcs(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();

        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i < m; i++) {
            Arrays.fill(dp[i], 0);
        }

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                }

                else if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }

                else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }

            // Print(dp);
        }

        return dp[m][n];
    }

    public static void main(String[] args) {
        String X = "AGGTAB";
        String Y = "GXTXAYB";

        System.out.println("Length of LCS is: " + lcs(X, Y));
    }
}