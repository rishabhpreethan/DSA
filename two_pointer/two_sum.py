#EASY

# 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
 
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


def twoSum(nums,target):
        p1=0
        p2=len(nums)-1
        while p1<p2:

            #if pointer 1 + pointer 2 is equal to the target then that is the answer
            if target==nums[p1]+nums[p2]:
                return [p1,p2]

            #if sum of numbers is less than the target then pointer 1 is incremented by one
            elif nums[p1]+nums[p2]<target:
                p1+=1

            #if sum of numbers is greater than the target then pointer 2 is decremented by one
            else:
                p2-=1

        #return false by default
        return False

print(twoSum([2,7,11,15],9))