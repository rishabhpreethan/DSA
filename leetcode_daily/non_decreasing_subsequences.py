#MEDIUM
# 491

'''     https://leetcode.com/problems/non-decreasing-subsequences/description/      ''' 

# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.


# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]


def findSubsequences(nums):
    sub = set()
    for num in nums:
        n = set()
        n.add((num,))
        for s in sub:
            if num >= s[-1]:
                n.add(s + (num,))
        sub |= n
    return [s for s in sub if len(s)>1]

print(findSubsequences([4,6,7,7]))