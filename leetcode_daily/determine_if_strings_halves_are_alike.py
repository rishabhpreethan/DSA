#EASY
# 1704

'''     https://leetcode.com/problems/determine-if-string-halves-are-alike/     '''

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.
 

# Example 1:
# Input: s = "book"
# Output: true
# ------------------------------------------------------------------------------------------------------------
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

# Example 2:
# Input: s = "textbook"
# Output: false
# -------------------------------------------------------------------------------------------------------------
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.



def halvesAreAlike(s):
    c1,c2=0,0
    l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    mid=int(len(s)/2)
    w1=s[:mid]
    w2=s[mid:]
    for i in w1:
        if i in l:
            c1+=1
    for i in w2:
        if i in l:
            c2+=1
    if c1==c2:
        return True
    return False

print(halvesAreAlike('book'))