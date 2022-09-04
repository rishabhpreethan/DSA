#EASY

# 461
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.


# Example 1:
# Input: x = 1, y = 4
# Output: 2
# -------------------------------------------
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
# Input: x = 3, y = 1
# Output: 1



def hammingDistance(x,y):
        first = str(bin(x))[2:]
        second = str(bin(y))[2:]
        l = 0
        while len(first) != len(second):
            if len(first) > len(second):
                second = '0' + second
            elif len(first) < len(second):
                first = '0' + first 
        for i in range(0,len(first)):
            if first[i] != second[i]:
                l = l + 1
        return l

print(hammingDistance(1,4))