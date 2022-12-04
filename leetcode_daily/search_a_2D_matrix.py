#MEDIUM
# 74


'''     https://leetcode.com/problems/search-a-2d-matrix/       '''


# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false



def searchMatrix(matrix,target):
    for i in matrix:
        n=len(i)
        l,r=0,len(i)-1
        while l<=r:
            mid=(l+r)//2
            if target<i[mid]:
                r=mid-1
            elif target>i[mid]:
                l=mid+1
            else:
                return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],20))