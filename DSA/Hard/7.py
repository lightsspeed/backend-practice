# This is 7.py

# Write a program to find the longest common subsequence (LCS) between two strings (e.g., "ABCDGH" and "AEDFHR").


def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
print(lcs("ABCDGH", "AEDFHR"))  # Output: 3 (e.g., "ADH")

print(lcs("AGGTAB", "GXTXAYB"))  # Output: 4 (e.g., "GTAB")
print(lcs("ABC", "AC"))  # Output: 2 (e.g., "AC")   