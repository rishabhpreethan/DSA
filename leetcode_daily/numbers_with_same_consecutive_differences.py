#MEDIUM

# 967
# Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.
# Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.
# You may return the answer in any order.


# Example 1:
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# ------------------------
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.

# Example 2:

# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


from collections import deque

def numsSameConsecDiff(n,k):
    ans = []
    que = deque([(1, i) for i in range(1, 10)])
    while que:
        pos, num = que.popleft()
        if pos == n:
            ans.append(num)
        else:
            less_digit = num % 10 - k
            greater_digit = num % 10 + k
            
            if less_digit >= 0:
                que.append((pos+1, num*10+less_digit))
            if less_digit != greater_digit and greater_digit < 10:
                que.append((pos+1, num*10+greater_digit))
            
    return ans

print(numsSameConsecDiff(3,7))