#MEDIUM
# 958

'''     https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/      '''

# Given the root of a binary tree, determine if it is a complete binary tree.
# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.


# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: true
# ---------------------------------------------------------------------
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

# Example 2:
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# ---------------------------------------------------------------------
# Explanation: The node with value 7 isn't as far left as possible.


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCompleteTree(self, root):
        queue=deque([root])
        while queue[0]:  
            node=queue.popleft()
            queue.extend([node.left,node.right])
        while queue and not queue[0]:
            queue.popleft()
        return not queue  