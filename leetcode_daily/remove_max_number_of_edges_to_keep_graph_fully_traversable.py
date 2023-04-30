#HARD
# 1579

'''     https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/       '''

# Alice and Bob have an undirected graph of n nodes and three types of edges:
# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can be traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.
# Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.


# Example 1:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# -----------------------------------------------------------
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.

# Example 2:
# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# -----------------------------------------------------------
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.

# Example 3:
# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# -----------------------------------------------------------
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.


def maxNumEdgesToRemove(n,edges):
    def find(i,r):
        if i!=r[i]:
            r[i]=find(r[i],r)
        return r[i]

    def uni(x,y,r):
        x,y=find(x,r),find(y,r)
        if x==y: 
            return 0
        r[x]=y
        return 1
    res=a=b=0
    r=list(range(n+1))
    for t,i,j in edges:
        if t==3:
            if uni(i,j,r):
                a+=1
                b+=1
            else:
                res += 1
    r0=r[:]
    for t,i,j in edges:
        if t==1:
            if uni(i,j,r):
                a+=1
            else:
                res+=1
    r=r0
    for t,i,j in edges:
        if t==2:
            if uni(i,j,r):
                b+=1
            else:
                res+=1
    if a==b==n-1:
        return res
    else:
        return -1
    
print(maxNumEdgesToRemove(4,[[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))