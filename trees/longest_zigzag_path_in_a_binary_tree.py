#MEDIUM
# 1372

'''     https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/     '''

# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.


# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# ------------------------------------------------------------------------------
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

# Example 2:
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# ------------------------------------------------------------------------------
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

# Example 3:
# Input: root = [1]
# Output: 0

def longestZigZag(self, root):
    def dfs(node):
        if not node:
            return [-1,-1,-1]
        l,r=dfs(node.left),dfs(node.right)
        return [l[1]+1,r[0]+1,max(l[1]+1,r[0]+1,l[2],r[2])]
    return dfs(root)[-1]