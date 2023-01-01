#EASY
# 290

'''     https://leetcode.com/problems/word-pattern/description/     '''

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


def wordPattern(pattern,s):
    d={}
    l=s.split()
    if len(pattern)!=len(l):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in d and l[i] not in d.values():
            d[pattern[i]]=l[i]
        if pattern[i] not in d.keys() or d[pattern[i]]!=l[i]:
            return False
    return True

print(wordPattern("abba","dog cat cat dog"))