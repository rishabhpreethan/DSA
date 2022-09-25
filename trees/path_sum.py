class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def is_leaf(self,node):
        if node.left == None and node.right == None:
            return True
        return False
    
    def hasPathSum(self, root, t: int):
        if root:
            
            if self.is_leaf(root):
                return t-root.val == 0
            
            l = self.hasPathSum(root.left, t-root.val)
            if l:
                return l
            
            r = self.hasPathSum(root.right, t-root.val)
            if r:
                return r
                    
        return False
    print(hasPathSum())