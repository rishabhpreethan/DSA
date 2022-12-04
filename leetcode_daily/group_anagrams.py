#MEDIUM

from collections import defaultdict

def groupAnagrams(strs):

    #creates a default dictionary with lists
    d=defaultdict(list)

    for i in strs:

        #every character from a-z mapped to 0
        count=[0]*26
        for c in i:

            #ascii value of current character - ascii value of 'a'  =  key
            count[ord(c)-ord('a')]+=1
        
        #tuple is immutable hence it can be used as a key
        d[tuple(count)].append(i)
    return d.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))