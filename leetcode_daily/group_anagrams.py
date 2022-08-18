#MEDIUM
from collections import defaultdict

def groupAnagrams(strs):
    d=defaultdict(list)
    for i in strs:
        count=[0]*26
        for c in i:
            count[ord(c)-ord('a')]+=1
        d[tuple(count)].append(i)
    return d.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))