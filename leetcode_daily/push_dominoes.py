#MEDIUM

# 838
# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:

# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.

 
# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# ------------------------------------------------------------------------------------
# Explanation: The first domino expends no additional force on the second domino.

# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."



def pushDominoes(dominoes):
    d=[]
    for i in dominoes:
        d.append(i)
        
    l=0
    r=len(d)-1
    f=0
    l=[]
    res=''
    
    for i in range(len(d)):
        if d[i]=='R':
            f=len(d)
        elif d[i]=='L':
            f=0
        else:
            f=max(f-1,0)
        l.append(f)
    
    for i in range(len(d)-1,-1,-1):
        if d[i]=='L':
            f=len(d)
        elif d[i]=='R':
            f=0
        else:
            f=max(f-1,0)
        l[i]-=f
        
    for i in l:
        if i>0:
            res+='R'
        elif i<0:
            res+='L'
        else:
            res+='.'
    return res

print(pushDominoes(".L.R...LR..L.."))