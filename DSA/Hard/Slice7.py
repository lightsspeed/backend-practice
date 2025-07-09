# This is Slice7.py

# Write a generator that yields the longest common subsequence (LCS) lengths for strings 'abcde' and 'ace' iteratively.


def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    for i in range(m + 1):
        yield max([lcs_length(str1[:i], str2[:j]) for j in range(n + 1)] + [0]) if i > 0 else 0
for length in lcs_length('abcde', 'ace'):
    print(length)  # Output: 0, 1, 1, 2, 2, 3 (simplified)