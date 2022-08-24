#MEDIUM

# 75
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.


# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]



def sortColors(nums):
    temp=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]<nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums

print(sortColors([2,0,2,1,1,0]))