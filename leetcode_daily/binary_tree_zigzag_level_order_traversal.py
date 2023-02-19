#MEDIUM
# 103

'''     https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/     '''

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self,root):
        if not root:
            return []

        queue=[root]
        res=[]
        level=0

        while queue:
            levelnodes=[]
            
            for i in range(len(queue)):
                node=queue.pop(0)
                levelnodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level%2==1:
                levelnodes.reverse()
            res.append(levelnodes)
            
            level+=1
        
        return res