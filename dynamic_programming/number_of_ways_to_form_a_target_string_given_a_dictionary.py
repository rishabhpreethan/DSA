# HARD
# 1639

'''     https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/        '''

# You are given a list of strings of the same length words and a string target.
# Your task is to form target using the given words under the following rules:
# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.
# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.


# Example 1:
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# --------------------------------------------------------------
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")

# Example 2:
# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# ----------------------------------------------------------------
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")


def numWays(words,target):
    n=len(words[0])
    m=len(target)
    mod=10**9+7
    dp=[0]*(m+1)
    dp[0]=1
    count=[[0] * 26 for _ in range(n)]
    for i in range(n):
        for word in words:
            count[i][ord(word[i])-ord('a')]+=1
    for i in range(n):
        for j in range(m-1,-1,-1):
            dp[j+1]+=dp[j]*count[i][ord(target[j])-ord('a')]
            dp[j+1]%=mod
    
    return dp[m]


print(numWays(["abba","baab"],"bab"))