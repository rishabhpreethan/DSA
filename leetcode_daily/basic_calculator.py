#HARD
# 224

'''     https://leetcode.com/problems/basic-calculator/     '''
'''     https://www.youtube.com/watch?v=A3noAzWZ9f4         '''

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


# Example 1:
# Input: s = "1 + 1"
# Output: 2

# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23


def calculate(s):
    stack=[]
    cur=0
    sign=1
    output=0
    for i in s:
        if i.isdigit():
            cur=cur*10+int(i)
            
        elif i in '+-':
            output+=cur*sign
            cur=0
            if i=='-':
                sign=-1
            else:
                sign=1
        
        elif i=='(':
            stack.append(output)
            stack.append(sign)
            output=0
            sign=1
        elif i==')':
            output+=(cur*sign)
            output*=stack.pop()
            output+=stack.pop()
            cur=0
    return output+(cur*sign)

print(calculate("(1+(4+5+2)-3)+(6+8)"))