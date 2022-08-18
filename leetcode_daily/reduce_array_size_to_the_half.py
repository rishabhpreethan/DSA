#MEDIUM

def minSetSize(arr):
    d = {}
    
    #making dictionary with number as key and its count as the value
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1  
    dv = list(d.values())
    ct = 0
    out = 0

    #sorting it in descending order
    dv.sort(reverse = True)
    for i in dv:
        ct+=i
        out+=1
        if ct>=len(arr)//2:
            return out
    
print(minSetSize([3,3,3,3,5,5,5,2,2,7]))