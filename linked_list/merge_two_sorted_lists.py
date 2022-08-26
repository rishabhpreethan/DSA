#EASY

# 21
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


def mergeTwoLists(self, l1, l2):
        dummy=ListNode()
        tail=dummy
        
        while l1 and l2:
            
            #if value of l1 lesser than value of l2
            if l1.val<l2.val:
                
                #next tail is equal to the l1 node
                tail.next=l1
                
                #l1 node is updated to the next node
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
                
            #tail is updated to the next node
            tail=tail.next
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
            
        return dummy.next
        