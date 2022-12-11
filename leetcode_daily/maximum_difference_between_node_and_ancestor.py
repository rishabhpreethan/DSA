#MEDIUM
# 1026


'''     https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/     '''


# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


# Example 1:
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# -----------------------------------------------------------------------------------------------
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

# Example 2:
# Input: root = [1,null,2,null,0,3]
# Output: 3



def maxAncestorDiff(self,root):
    result = [0]
    self.traverse(root, root.val, root.val, result)
    return result[0]

def traverse(self, root, low, high, result):
    if not root:
        return
    result[0] = max(result[0], abs(root.val - low) , abs(root.val-high) )
    if root.val < low:
        low = root.val
    if root.val > high:
        high = root.val
    self.traverse(root.left, low, high, result)
    self.traverse(root.right, low, high, result)
    
print(maxAncestorDiff([1,0,2,0,0,3]))