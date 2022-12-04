#EASY

d={}
s='leetcode'
for i in s:
    d[i]=0
for i in s:
    d[i]+=1
for e in d:
    if d[e]==1:
         print(s.index(e))
         break
