# This is Tuple1.py

# Write a function to find the longest common subsequence between two tuples.


def longest_common_subsequence(tup1, tup2):
    m, n = len(tup1), len(tup2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif tup1[i-1] == tup2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
print(longest_common_subsequence((1, 2, 3), (2, 3, 4)))  # Output: 2