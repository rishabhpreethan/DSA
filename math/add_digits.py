#EASY
# 258


'''     https://leetcode.com/problems/add-digits/description/       '''


# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


# Example 1:
# Input: num = 38
# Output: 2
# -----------------------------------------
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0


def addDigits(num):
    if num==0:
        return 0
    elif num%9==0:
        return 9
    else:
        return num%9
    
print(addDigits(38))