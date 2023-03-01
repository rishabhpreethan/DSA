#MEDIUM
# 912

'''     https://leetcode.com/problems/sort-an-array/description/        '''

# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# ----------------------------------------------------------
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# ----------------------------------------------------------
# Explanation: Note that the values of nums are not necessairly unique.


import random

def sortArray(nums):
    def quicksort(nums):
        if len(nums)<=1: 
            return nums
        pivot=random.choice(nums)
        l,e,g=[],[],[]
        for val in nums:
            if val<pivot: 
                l.append(val)
            elif val>pivot: 
                g.append(val)
            else: 
                e.append(val)
        return quicksort(l)+e+quicksort(g)
    return quicksort(nums)

print(sortArray([5,1,1,2,0,0]))