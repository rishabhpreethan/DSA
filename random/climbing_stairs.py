#EASY

# 70
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# ---------
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# ---------
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(self,n):
        # base case - reached last stair
        if n==0:
            return 1
        elif n<0:
            return 0

        #allowed to take one or two steps at a time
        return self.climbStairs(n-1)+self.climbStairs(n-2)

print(climbStairs(self,3))