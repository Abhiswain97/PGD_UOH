#include <stdio.h>
#include <string.h>

int max(int a, int b) { return (a > b) ? a : b; }

int lcs(char s1[], char s2[], int m, int n)
{

    int L[100][100];

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            L[i][j] = 0;
        }
    }

    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            if (i == 0 || j == 0)
                L[i][j] = 0;

            else if (s1[i - 1] == s2[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;

            else
                L[i][j] = max(L[i][j - 1], L[i - 1][j]);
        }
    }

    return L[m][n];
}

int main(int argc, char const *argv[])
{
    char X[] = "AGGTAB";
    char Y[] = "GXTXAYB";

    int m = strlen(X);
    int n = strlen(Y);

    printf("Length of LCS is %d", lcs(X, Y, m, n));
    return 0;
}
