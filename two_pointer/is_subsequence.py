#EASY

# 392
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


def isSubsequence(s,t):
    l=0
    r=0
    
    if len(s) == 0 and len(t) == 0:
        return True 
    
    if len(s) == 0 and len(t) != 0:
        return True 
    
    if len(s) != 0 and len(t) == 0:
        return False 
    
    while l<len(s) and r<len(t):
        if s[l]==t[r]:
            l+=1
        r+=1
    return l == len(s)

print(isSubsequence("abc","ahbgdc"))