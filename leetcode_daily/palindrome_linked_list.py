#EASY

# 234
# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false



def isPalindrome(head):
    l=[]
    while head:
        l.append(head.val)
        head=head.next
    return l==l[::-1]

print(isPalindrome([1,2,2,1]))