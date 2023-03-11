#EASY
# 110

'''     https://leetcode.com/problems/balanced-binary-tree/description/     '''

# Given a binary tree, determine if it is 
# height-balanced


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root):
    
        def dfs(root):
            if not root:
                return [True,0]

            left=dfs(root.left)
            right=dfs(root.right)
            flag=(left[0] and right [0] and abs(left[1]-right[1])<=1)    
            return [flag,1+max(left[1],right[1])]
        return dfs(root)[0]