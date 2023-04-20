# MEDIUM
# 662

'''     https://leetcode.com/problems/maximum-width-of-binary-tree/description/     '''

# Given the root of a binary tree, return the maximum width of the given tree.
# The maximum width of a tree is the maximum width among all levels.
# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
# It is guaranteed that the answer will in the range of a 32-bit signed integer.


# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# --------------------------------------------------------------------------------
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# --------------------------------------------------------------------------------
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

# Example 3:
# Input: root = [1,3,2,5]
# Output: 2
# --------------------------------------------------------------------------------
# Explanation: The maximum width exists in the second level with length 2 (3,2).


from collections import deque

def widthOfBinaryTree(self,root):
    q=deque([(root,0)])
    w=0
    while q:
        w=max(w,q[-1][1]-q[0][1])
        for _ in range(len(q)):
            node,k=q.popleft()
            if node.left:
                q.append((node.left,k*2-1))
            if node.right:
                q.append((node.right,k*2))
    return w+1