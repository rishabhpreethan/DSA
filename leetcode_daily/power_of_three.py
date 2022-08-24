#EASY

# 326
# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.


# Example 1:
# Input: n = 27
# Output: true

# Example 2:
# Input: n = 0
# Output: false

# Example 3:
# Input: n = 9
# Output: true


def isPowerOfThree(n):
    a=1
    while a<n:
        a*=3
    if a==n:
        return True
    else:
        return False

print(isPowerOfThree(27))