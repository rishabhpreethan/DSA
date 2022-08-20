#EASY

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
#---------
# Explanation: [4,9] is also accepted.


def intersection(nums1,nums2):
        l=[]
        s1=set(nums1)
        s2=set(nums2)
        for i in s1:
            if i in s2:
                l.append(i)
        for i in s2:
            if i in s1:
                l.append(i)
        return set(l)
    
    
        #OR
        
        
        # return s1.intersection(s2)


print(intersection([1,2,2,1],[2,2]))