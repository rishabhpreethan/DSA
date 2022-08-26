#MEDIUM

# 869
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
# Return true if and only if we can do this so that the resulting number is a power of two.


# Example 1:
# Input: n = 1
# Output: true

# Example 2:
# Input: n = 10
# Output: false



from collections import Counter
def reorderedPowerOf2(n):
        c = Counter([int(i) for i in str(n)])
        N, i = 0,0
        while N <= 10**9:
            N = 2 ** i
            d = Counter([int(i) for i in str(N)])
            if c == d: return True
            i += 1
        return False

print(reorderedPowerOf2(46))