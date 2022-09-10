#HARD


# 188
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# ---------------------
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# ----------------------
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


def maxProfit(k,prices):
        min_price = [float("inf")] * (k + 1)
        max_profit = [0] * (k + 1)
        
        for price in prices:
            for i in range(1, k + 1):
                min_price[i] = min(min_price[i], price - max_profit[i-1])
                max_profit[i] = max(max_profit[i], price - min_price[i])

        return max_profit[k]

print(maxProfit(2,[2,4,1]))