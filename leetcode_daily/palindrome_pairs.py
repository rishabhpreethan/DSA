#HARD

'''     https://leetcode.com/problems/palindrome-pairs/     '''

# 336
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.


# Example 1:
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# ------------------------------------------------------
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# ------------------------------------------------------
# Explanation: The palindromes are ["battab","tabbat"]

# Example 3:
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]



def palindromePairs(words):
    rmap = {w[::-1]:i for i,w in enumerate(words)}
    res = []
    for i,w in enumerate(words):
        if w in rmap:
            if rmap[w] != i:
                res.append([i,rmap[w]])
        for j in range(1,len(w)+1):
            if w[:-j] in rmap and w[-j:] == w[-j:][::-1]:
                    res.append([i,rmap[w[:-j]]])
            if w[j:] in rmap and w[:j] == w[:j][::-1]:
                res.append([rmap[w[j:]],i])
    return res

print(palindromePairs(["abcd","dcba","lls","s","sssll"]))