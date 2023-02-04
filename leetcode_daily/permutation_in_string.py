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


from itertools import permutations

def checkInclusion(s1,s2):
    words = [''.join(p) for p in permutations(s1)]
    # print(words)
    l=0
    r=len(s1)
    while r<=len(s2):
        # print('l,r: ',l,r)
        if s2[l:r] in words:
            return True
        else:
            l+=1
            r+=1
    return False

print(checkInclusion("ab","eidbaooo"))