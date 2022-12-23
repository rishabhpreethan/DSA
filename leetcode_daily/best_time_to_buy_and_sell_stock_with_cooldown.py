#MEDIUM
# 309

'''     https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/        '''

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: prices = [1,2,3,0,2]
# Output: 3
# ----------------------------------------------------------------
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# Example 2:
# Input: prices = [1]
# Output: 0


def maxProfit(p):
    if not p:
        return 0
    n=len(p)
    dp=[0]*(n+1)
    minp=p[0]
    for i in range(1,n+1):
        minp=min(minp,p[i-1]-dp[i-2])
        dp[i]=max(dp[i-1],p[i-1]-minp)
    return dp[n]

print(maxProfit([1,2,3,0,2]))