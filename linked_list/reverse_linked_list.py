#EASY

# 206
# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []



def reverseList(head):
    prev=None 
    curr=head
    while curr:
        t=curr.next
        curr.next=prev
        prev=curr
        curr=t
    return prev
print(reverseList([1,2,3,4,5]))