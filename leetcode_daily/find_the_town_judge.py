#EASY
# 997

'''     https://leetcode.com/problems/find-the-town-judge/      '''

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


# Example 1:
# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:
# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:
# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1


from collections import defaultdict

def findJudge(n,trust) -> int:
    d1=defaultdict(int)
    d2=defaultdict(int)
    for i,j in trust:
        d1[i]+=1
        d2[j]+=1
    for i in range(1,n+1):
        if d2[i]==n-1 and d1[i]==0:
            return i
    return -1

print(findJudge(3,[[1,3],[2,3]]))