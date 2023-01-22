#MEDIUM
# 131

'''     https://leetcode.com/problems/palindrome-partitioning/description/      '''

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]


def partition(self,s):
    res = []
    path = []
    self.func(0, s, res, path)
    return res

def func(self, ind, s, res, path):
    if ind == len(s):
        res.append(path[:])
        return 
    for i in range(ind, len(s)):
        if self.isPalindrome(s, ind, i):
            path.append(s[ind:i+1])
            self.func(i+1, s, res, path)
            path.pop()

def isPalindrome(self, s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(partition(self,"aab"))