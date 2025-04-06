# This is list3.py

# Write a program to find the longest increasing subsequence in a list.


def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101]))  # Output: 4