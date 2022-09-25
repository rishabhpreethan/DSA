#EASY

# 350
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# --------------------------------------------------------
# Explanation: [9,4] is also accepted.


def intersect(nums1,nums2):
    nums1.sort()
    nums2.sort()
    l=0
    r=0
    nl=[]
    while l<len(nums1) and r<len(nums2):
        
        if nums1[l]<nums2[r]:
            l+=1
            
        elif nums1[l]>nums2[r]:
            r+=1
            
        else:
            nl.append(nums1[l])
            l+=1
            r+=1
    return nl

print(intersect([1,2,2,1],[2,2]))