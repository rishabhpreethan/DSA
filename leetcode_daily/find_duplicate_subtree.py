#MEDIUM
# 652

'''     https://leetcode.com/problems/find-duplicate-subtrees/description/      '''

# Given the root of a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
# Two trees are duplicate if they have the same structure with the same node values.


# Example 1:
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

# Example 2:
# Input: root = [2,1,1]
# Output: [[1]]

# Example 3:
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, d, duplicates):
        if not root:
            return '.'
        subtree=str(root.val)+'-'+self.dfs(root.left,d,duplicates)+'-'+self.dfs(root.right,d,duplicates)
        if subtree in d:
            if d[subtree]==1:
                duplicates.append(root)
            d[subtree]+=1
        else:
            d[subtree]=1
        return subtree
    
    def findDuplicateSubtrees(self,root):    
        d,duplicates={},[]
        self.dfs(root,d,duplicates)
        return duplicates