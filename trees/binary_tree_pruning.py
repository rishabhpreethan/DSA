#MEDIUM

# 814
# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.


# Example 1:
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# ------------------------------------------
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.

# Example 2:
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]

# Example 3:
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]



def pruneTree(self, root):
    def prune(root):
        if root==None:
            return 0
        left=prune(root.left)
        right=prune(root.right)
        if left==0:
            root.left=None
        if right==0:
            root.right=None
        if left==right==0:
            return root.val
        if left==1 or right==1:
            return 1
    temp=prune(root)
    if temp==0:
        return None
    return root