# MEDIUM
# 209

'''     https://leetcode.com/problems/minimum-size-subarray-sum/description/        '''

# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# ----------------------------------------------------------
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


def minSubArrayLen(target,nums):
    p1=0
    total=0
    mi=float('inf')
    for p2 in range(len(nums)):
        total+=nums[p2]
        while total>=target:
            mi=min(mi,p2-p1+1)
            total-=nums[p1]
            p1+=1
    if mi>target:
        return 0
    return mi

print(minSubArrayLen(7,[2,3,1,2,4,3]))