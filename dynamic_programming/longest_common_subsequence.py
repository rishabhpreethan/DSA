#MEDIUM
# 1143

'''     https://leetcode.com/problems/longest-common-subsequence/       '''

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# --------------------------------------------------------------------------
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# ----------------------------------------------------------------------------
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# ---------------------------------------------------------------------------
# Explanation: There is no such common subsequence, so the result is 0.


def longestCommonSubsequence(text1,text2):
    dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            if text2[i-1] == text1[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 
    return dp[-1][-1]

print(longestCommonSubsequence("abcde","ace"))