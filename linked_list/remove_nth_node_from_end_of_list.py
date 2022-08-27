#MEDIUM

# 19
# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]


def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        left=dummy
        right=head
        
        while n>0:
            right=right.next
            n-=1
        
        while right:
            left=left.next
            right=right.next
            
        left.next=left.next.next
        return dummy.next