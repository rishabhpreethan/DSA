#MEDIUM

#53
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.


# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23


def maxSubArray(nums):
    s=0
    m=nums[0]
    for i in nums:
        s+=i

        #if s is greater than m then m is replaced b s value
        if m<s:
            m=s
        
        #if s is less than 0 then it is equal to 0
        if s<0:
            s=0
    return m

print(maxSubArray[-2,1,-3,4,-1,2,1,-5,4])