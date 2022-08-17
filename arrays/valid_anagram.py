d1={}
d2={}
s='anagram'
t='nagaram'

#creating dictionaries with count of letters of string 1
for i in s:
    d1[i]=0
for i in s:
    d1[i]+=1

#for string two
for i in t:
    d2[i]=0
for i in t:
    d2[i]+=1

#prints true if both dictionaries are equal
if d1==d2:
    print(True)
else:
    print(False)
