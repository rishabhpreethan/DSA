#HARD
# 2444

'''     https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/        '''

# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
# A subarray is a contiguous part of an array.


# Example 1:
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# ----------------------------------------------------------------------------
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# ----------------------------------------------------------------------------
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


def countSubarrays(nums,minK,maxK):
    n=len(nums)
    l=-1
    mi,ma=-1,-1
    c=0
    for i in range(n):
        if nums[i]>=minK and nums[i]<=maxK:
            mi=i if nums[i]==minK else mi
            ma=i if nums[i]==maxK else ma
            c+=max(0,min(mi,ma)-l)
        else:
            l=i
            mi=-1
            ma=-1
    return c

print(countSubarrays([1,3,5,2,7,5],1,5))