#MEDIUM

# 985
# You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
# For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
# Return an integer array answer where answer[i] is the answer to the ith query.


# Example 1:
# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# ---------------------------------------------------------------------
# Explanation: At the beginning, the array is [1,2,3,4].
# After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.

# Example 2:
# Input: nums = [1], queries = [[4,0]]
# Output: [0]


def sumEvenAfterQueries(nums,q):
    l=[]
    nl=[]
    s=0
    for j in q:
        nums[j[1]]+=j[0]
        for i in nums:
            if i%2==0:
                s+=i    
        l.append(s)
        s=0
    return l


print(sumEvenAfterQueries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))