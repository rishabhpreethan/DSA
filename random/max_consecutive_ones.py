#EASY

# 485
# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# --------------------------------
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2



def findMaxConsecutiveOnes(nums):
    m=0
    s=0
    for i in nums:
        if i==1:
            s+=1
        else:
            s=0
        m=max(s,m)
    return m

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))