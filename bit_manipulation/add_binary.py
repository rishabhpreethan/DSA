#EASY
# 67

'''     https://leetcode.com/problems/add-binary/description/       '''

# Given two binary strings a and b, return their sum as a binary string.


# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


import time

def addBinary(a,b):
    res=""
    c=0
    a,b=a[::-1],b[::-1]

    for i in range(max(len(a),len(b))):
        A=ord(a[i])-ord("0") if i<len(a) else 0
        B=ord(b[i])-ord("0") if i<len(b) else 0
        total=A+B+c
        ch=str(total%2)
        res=ch+res
        c=total//2
    if c:
        return "1"+res
    return res


a=time.time()
print(addBinary("1010","1011"))
b=time.time()
print("Time taken: ",b-a)

# Time Complexity : O(n)