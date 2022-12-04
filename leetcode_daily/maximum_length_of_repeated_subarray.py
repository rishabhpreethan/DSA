#MEDIUM

# 718
# Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.


# Example 1:

# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# --------------------------------------------------------
# Explanation: The repeated subarray with maximum length is [3,2,1].

# Example 2:
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5



def findLength(nums1,nums2):
    dp=[[0]*(len(nums2)+1) for i in range(len(nums1)+1)]
    ans=0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
                ans = max(ans, dp[i+1][j+1])

    return ans

print(findLength([1,2,3,2,1],[3,2,1,4,7]))
# print(findLength([0,0,0,0,0],[0,0,0,0,0]))