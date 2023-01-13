#HARD
# 2246

'''     https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/      '''

# You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
# You are also given a string s of length n, where s[i] is the character assigned to node i.
# Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.


# Example 1:
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# -----------------------------------------------------------------
# Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the conditions. 

# Example 2:
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# -----------------------------------------------------------------
# Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.


from collections import defaultdict

def longestPath(self,parent,s):
    d=defaultdict(list)
    for i,u in enumerate(parent):
        d[u].append(i)
    self.ans=0
    def dfs(root):
        a1=a2=0
        for v in d[root]:
            if s[v]==s[root]:
                dfs(v)
                continue
            curr=dfs(v)
            if curr>=a1:
                a2=a1
                a1=curr
            elif curr>=a2:
                a2=curr
        self.ans=max(self.ans, a1 + a2 + 1)
        return a1+1
    dfs(0)        
    return self.ans

print(longestPath([-1,0,0,0],"aabc"))