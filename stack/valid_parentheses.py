#EASY

# 20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


def isValid(s):
    d={']':'[','}':'{',')':'('}
    st=[]
    for i in s:
        if i not in d:
            st.append(i)
            continue
        if not st or st[-1]!=d[i]:
            return False
        st.pop()
    return not st

print(isValid('()[]{}'))