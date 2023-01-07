# 625 root is 25
# last digits should be equal to its root - automorhic number


import math

def automorphicNumber(n):
    sq=math.sqrt(n)
    sq=str(int(sq))
    n=str(n)
    s=str(n[len(n)-len(sq):len(n)])
    if s==sq:
        return True
    else:
        return False
    
print(automorphicNumber(625))