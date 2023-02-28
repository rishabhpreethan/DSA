#MEDIUM
# 179

'''     https://leetcode.com/problems/largest-number/description/       '''

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.


# Example 1:
# Input: nums = [10,2]
# Output: "210"

# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"

from functools import cmp_to_key

def largestNumber(nums):
    l=len(nums)
    s=''
    for i in range(l):
        nums[i]=str(nums[i])

    def isgreater(n1,n2):
        if n1+n2>n2+n1:
            return -1
        else:
            return 1

    nums=sorted(nums,key=cmp_to_key(isgreater))
    for i in nums:
        s+=i
    return str(int(s))

print(largestNumber([3,30,34,5,9]))