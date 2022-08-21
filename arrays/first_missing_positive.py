#HARD

#O(N)

# 41
# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.
 
# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# ---------
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# ---------
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# ---------
# Explanation: The smallest positive integer 1 is missing.


def firstMissingPositive(nums):
        l = len(nums)
        for i in range(l):
            if nums[i] <= 0 or nums[i] > l:
                nums[i] = 0
        for i in range(l):
            if nums[i] > 0 and nums[nums[i]-1] >= 0:
                nums[nums[i]-1] = -1-nums[nums[i]-1]
            elif nums[i] < -1 and nums[-nums[i]-2] >= 0:
                nums[-nums[i]-2] = -1-nums[-nums[i]-2]
        for i in range(l):
            if nums[i] >= 0:
                return i+1
        return l+1

print(firstMissingPositive([1,2,0]))