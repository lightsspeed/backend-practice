# This is Tuple8.py

# Create a function to find the longest increasing subsequence in a tuple.


def longest_increasing_subsequence(tup):
    n = len(tup)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if tup[i] > tup[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(longest_increasing_subsequence((10, 9, 2, 5, 3, 7)))  # Output: 3