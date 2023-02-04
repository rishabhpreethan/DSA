#MEDIUM
# 6


'''     https://leetcode.com/problems/zigzag-conversion/description/        '''


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);


# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"


def convert(s,row):
    n=len(s)
    if n<=row:
        return s
    ans,startIndex,idx,flag,count='',0,0,0,2
    for i in range(n):
        if startIndex==0 or startIndex==row-1:
            ans+=s[idx]
            idx+=row + (row - 2)
            if i==n-1: 
                break
            if idx>n-1 or idx<=0:
                startIndex+=1
                idx=startIndex
        else:
            if flag==0:
                ans+=s[idx]
                flag=1
                idx+=row+(row-2)-count
            else:
                ans+=s[idx]
                idx+=count
                flag=0
            if idx>n-1 or idx<=0:
                startIndex+=1
                idx,flag=startIndex,0
                count+=2
    return ans

print(convert("PAYPALISHIRING",3))