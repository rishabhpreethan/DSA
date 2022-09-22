#EASY

# 345
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.


# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"



def reverseVowels(s):
    l=0
    r=len(s)-1
    l1=[]
    n=''
    vowels=["a","e","i","o","u","A","E","I","O","U"]
    for i in s:
        l1.append(i)
    while l<=r:
        if l1[l] in vowels and l1[r] in vowels:
            l1[l],l1[r]=l1[r],l1[l]
            l+=1
            r-=1
        elif l1[l] in vowels and l1[r] not in vowels:
            r-=1
        elif l1[r] in vowels and l1[l] not in vowels:
            l+=1
        else:
            l+=1
            r-=1
    for i in l1:
        n+=i
        
    return n

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))