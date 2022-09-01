#MEDIUM

""" SOLVED USING FLOYD'S TORTOISE AND HARE """

#refer:
# https://youtu.be/9YTjXqqJEFE


# 287
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3



def findDuplicate(nums):

    # two poiters representing the tortoise and hare starting at the same point
    t=nums[0]
    h=nums[0]

    while True:

        #to find the cycle
        t=nums[t]
        h=nums[nums[h]]

        #meeting point of the tortoise and hare
        if t==h:
            break
        
    #pointer one starts at the start of the the list
    p1=nums[0]

    #pointer two starts at the meeting point of the tortoise and the hare
    p2=t

    while p1!=p2:
        
        #if the length of the starting point to the start of the cylce is equal to the
        #length of the meeting point to the start of the cycle then the new meeting point is the answer
        p1=nums[p1]
        p2=nums[p2]
        
    return p2



print(findDuplicate([3,1,3,4,2]))
# print(findDuplicate([1,4,3,5,6,1,2]))