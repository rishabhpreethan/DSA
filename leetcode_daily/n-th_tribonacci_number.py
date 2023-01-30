#EASY
# 1137

'''     https://leetcode.com/problems/n-th-tribonacci-number/description/       ''' 

# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.


# Example 1:
# Input: n = 4
# Output: 4
# ----------------------------------
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# Example 2:
# Input: n = 25
# Output: 1389537


def tribonacci(n):
    a=0
    b=1
    c=1
    t=[0,1,1]
    if n<3:
        return t[n]
    for i in range(3, n+1):
        s=a+b+c
        a=b
        b=c
        c=s
    return s

print(tribonacci(25))