#EASY
# 338

'''     https://leetcode.com/problems/counting-bits/description/        '''

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


# Example 1:
# Input: n = 2
# Output: [0,1,1]
# ----------------------------------
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# ----------------------------------
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101


def countBits(n):
    dp = [0] * (n+1)
    o = 1

    for i in range(1,n+1):
        if o * 2 == i:
            o = i
        dp[i] = 1 + dp[i - o]
    return dp

print(countBits(5))