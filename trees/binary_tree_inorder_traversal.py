#EASY

# 94
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]


def inorderTraversal(self, root):
        r=[]
        if root:
            r.extend(self.inorderTraversal(root.left))
            r.append(root.val)
            r.extend(self.inorderTraversal(root.right))
        return r