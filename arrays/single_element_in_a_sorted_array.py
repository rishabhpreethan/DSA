#MEDIUM
# 540

'''     https://leetcode.com/problems/single-element-in-a-sorted-array/description/     '''

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.


# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10


def singleNonDuplicate(nums):
    l=0
    r=len(nums)-1

    if r==0:
        return nums[0]
    elif nums[0]!=nums[1]:
        return nums[0]
    elif nums[r]!=nums[r-1]:
        return nums[r]
    
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]
        elif (nums[mid]==nums[mid-1] and mid%2==1) or (mid%2==0 and nums[mid]==nums[mid+1]):
            l=mid+1
        else:
            r=mid-1
    return nums[mid]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))