#HARD
# 1312

'''     https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/      '''

# Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.


# Example 1:
# Input: s = "zzazz"
# Output: 0
# ----------------------------------------------------------------------------------
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.

# Example 2:
# Input: s = "mbadm"
# Output: 2
# ----------------------------------------------------------------------------------
# Explanation: String can be "mbdadbm" or "mdbabdm".

# Example 3:
# Input: s = "leetcode"
# Output: 5
# ----------------------------------------------------------------------------------
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".


def minInsertions(s):
    if s==s[::-1]: 
        return 0 
    n=len(s)
    dp=[[0]*n for _ in range(n)]
    for i in range(n-1,-1,-1):
        dp[i][i]=1
        for j in range(i+1,n):
            if s[i]==s[j]:dp[i][j]=dp[i+1][j-1]+2
            else: dp[i][j]=max(dp[i+1][j], dp[i][j-1])
    return n-dp[0][n-1]


print(minInsertions("mbadm"))