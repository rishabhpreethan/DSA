#EASY
# 953

'''     https://leetcode.com/problems/verifying-an-alien-dictionary/        '''

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.


# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true

# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false

# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false

# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character.


def isAlienSorted(words,order):
    d=dict()
    for inx,c in enumerate(order):
        d[c]=inx
    for j in range(1,len(words)):
        cl=len(words[j])
        pl=len(words[j-1])
        p,q=0,0
        while p<cl and q<pl:
            if d[words[j][p]]<d[words[j-1][q]]:
                return False
            if d[words[j][p]]>d[words[j-1][q]]:
                break
            p+=1
            q+=1
        if p==cl and q<pl:
            return False        
    return True

print(isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))