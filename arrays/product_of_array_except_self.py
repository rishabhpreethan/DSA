#MEDIUM

#238

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]



def productExceptSelf(nums):

    #creating a list of length of nums with 1's
    l=[1]*len(nums)

    #prefix
    #run code to see whats happening
    pre=1
    for i in range(len(nums)):
        l[i]=pre
        pre*=nums[i]
        print('pre: ',l)

    post=1
    for i in range(len(nums)-1,-1,-1):
        l[i]*=post
        post*=nums[i]
        print('post: ',l)
    return l

productExceptSelf([1,2,3,4])