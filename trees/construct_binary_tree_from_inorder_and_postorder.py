#MEDIUM
# 106

'''     https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/       '''

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self,inorder,postorder):
        d = {ch : i for i, ch in enumerate(inorder)}
        self.rootIndex=len(postorder)-1
        def solve(l,r):
            if l>r: 
                return None
            root=TreeNode(postorder[self.rootIndex]) 
            self.rootIndex-=1
            i=d[root.val]
            root.right=solve(i+1,r)
            root.left=solve(l,i-1)
            return root
        return solve(0,len(inorder)-1)