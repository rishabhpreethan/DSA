#MEDIUM
# 567

'''     https://leetcode.com/problems/permutation-in-string/description/        '''

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.


# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


from collections import Counter

def checkInclusion(s1,s2):
    w=len(s1)
    s1c=Counter(s1)
    for i in range(len(s2)-w+1):
        s2c=Counter(s2[i:i+w])
        if s2c==s1c:
            return True

print(checkInclusion("ab","eidbaooo"))