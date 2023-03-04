#MEDIUM
# 28

'''     https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/       '''

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# -------------------------------------------------------------
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# -------------------------------------------------------------
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


def strStr(haystack,needle):
    l=0
    r=len(needle)
    if haystack==needle:
        return 0
    if len(needle)==1:
        for i in range(len(haystack)):
            if haystack[i]==needle:
                return i
    while r<=len(haystack):
        if haystack[l:r]==needle:
            return l
        else:
            l+=1
            r+=1
    return -1

print(strStr("sadbutsad","sad"))