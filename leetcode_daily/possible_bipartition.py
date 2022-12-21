#MEDIUM
# 886

'''     https://leetcode.com/problems/possible-bipartition/     '''

# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


# Example 1:
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# --------------------------------------------------
# Explanation: group1 [1,4] and group2 [2,3].

# Example 2:
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false

import collections

def possibleBipartition(N,dislikes):
    def dfs(node, color, colorGraph):
        
        if( node in colorGraph and colorGraph[node] == color ^ 1 ):
            return False
        
        if( node in colorGraph ):
            return True
        
        colorGraph[ node ] = color
        
        for nei in dislike_graph[ node ]:
            if not dfs( nei, color ^ 1, colorGraph ):
                return False
        
        return True
            
    
    if(not dislikes):   return True
    dislike_graph = collections.defaultdict(list)
    for u, v in dislikes:
        dislike_graph[ u ].append( v )
        dislike_graph[ v ].append( u )
    
    color = 0
    colorGraph = {}
    for i in range(1, N+1):
        if i not in colorGraph:
            if not dfs( i, color, colorGraph ):
                return False
    return True
    
print(possibleBipartition(4,[[1,2],[1,3],[2,4]]))