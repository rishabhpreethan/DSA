#EASY
# 783

'''     https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/       '''

# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.


# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1


def minDiffInBST(root):
    res=[]
    def d(root):
        if root:
            d(root.right)
            d(root.left)
            res.append(root.val)
    d(root)
    res.sort()
    l=len(res)
    return min([res[i]-res[i-1] for i in range(1,l)])