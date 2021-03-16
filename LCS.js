lcs = (s1, s2) => {
	m = s1.length;
	n = s2.length;

	dp = Array(m + 1)
		.fill(0)
		.map((n) => Array(n + 1).fill(0));

	for (let i = 0; i <= s1.length; i++) {
		for (let j = 0; j <= s2.length; j++) {
			if (i == 0 || j == 0) {
				dp[i][j] = 0;
			} else if (s1[i - 1] == s2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			} else {
				dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
			}
		}
	}

	return dp[m][n];
};

X = 'AGGTAB';
Y = 'GXTXAYB';
console.log('Length of LCS is ', lcs(X, Y));
