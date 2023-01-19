#MEDIUM
# 974

'''     https://leetcode.com/problems/subarray-sums-divisible-by-k/description/     '''

# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.


# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# ----------------------------------------------------------------------
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# Example 2:
# Input: nums = [5], k = 9
# Output: 0


from collections import defaultdict

def subarraysDivByK(nums,k):
    freq=defaultdict(int)
    freq[0]=1
    res=s=0
    for n in nums:
        s+=n
        r=s%k
        res+=freq[r]
        freq[r]+=1
    return res

print(subarraysDivByK([4,5,0,-2,-3,1],5))