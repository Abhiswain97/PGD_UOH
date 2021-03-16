function lcs(s1::String, s2::String)
    dp = zeros(Int8, length(s1) + 1, length(s2) + 1)

    for i = 1:(length(s1) + 1)
        for j = 1:(length(s2) + 1)
            if i == 1 || j == 1
                dp[i, j] = 0
            elseif s1[i - 1] == s2[j - 1]
                dp[i, j] = dp[i - 1, j - 1] + 1
            else
                dp[i, j] = max(dp[i, j - 1], dp[i - 1, j])
            end            
        end
    end

    return dp[length(s1) + 1, length(s2) + 1]
end

X = "AGGTAB"
Y = "GXTXAYB"

println("Length of lcs is: ", lcs(X, Y))

