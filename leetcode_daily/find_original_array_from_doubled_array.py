#MEDIUM

# 2007
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.


# Example 1:
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# --------------------------------------
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].

# Example 2:
# Input: changed = [6,3,0,1]
# Output: []
# --------------------------------------
# Explanation: changed is not a doubled array.

# Example 3:
# Input: changed = [1]
# Output: []
# --------------------------------------
# Explanation: changed is not a doubled array.



from collections import deque


def findOriginalArray(changed):
    changed.sort()
    s=deque([])
    res=[]
    
    for i in changed:
        if s and s[0]*2==i:
            b=s.popleft()
            res.append(b)
        else:
            s.append(i)
    return res if not s else []

print(findOriginalArray([1,3,4,2,6,8]))