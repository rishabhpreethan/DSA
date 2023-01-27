#HARD 
# 472

'''     https://leetcode.com/problems/concatenated-words/description/       '''

# Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.


# Example 1:
# Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# -----------------------------------------------------------------
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

# Example 2:
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]


def findAllConcatenatedWordsInADict(words):
    seen=set(words)
    def fn(word):
        for i in range(1,len(word)): 
            prefix=word[:i]
            suffix=word[i:]
            if (prefix in seen) and (suffix in seen or fn(suffix)): 
                return True 
        return False 
    ans=[]
    for word in words: 
        if fn(word): 
            ans.append(word)
    return ans

print(findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))