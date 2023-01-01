#EASY
# 205

'''     https://leetcode.com/problems/isomorphic-strings/description/       '''

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true


def isIsomorphic(s,t):
    d={}
    if len(s)!=len(t):
        return False
    for i in range(len(s)):
        if s[i] not in d and t[i] not in d.values():
            d[s[i]]=t[i]
        if s[i] not in d.keys() or d[s[i]]!=t[i]:
            return False
    return True

print(isIsomorphic("egg","add"))