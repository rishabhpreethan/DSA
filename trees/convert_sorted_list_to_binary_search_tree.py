#MEDIUM
# 109

'''     https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/        '''

# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
# height-balanced
# binary search tree.


# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

# Example 2:
# Input: head = []
# Output: []


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedListToBST(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        print(arr)
        def help(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root=TreeNode(arr[m])
            root.left=help(l,m-1)
            root.right=help(m+1,r)
            return root
        return help(0,len(arr)-1)