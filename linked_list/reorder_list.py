#MEDIUM

# 143
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]



def reorderList(self, head):
        slow=head
        fast=head.next

        #finding the middle of the linked list
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        second=slow.next
        slow.next=None      #splitting the linked list into two
        prev=None

        #reversing the second half of the linked list
        while second:
            t=second.next
            second.next=prev
            prev=second
            second=t
            
            
        first=head   
        second=prev

        #merging the first and second linked lists
        while second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2