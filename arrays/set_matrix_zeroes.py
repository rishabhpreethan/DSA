#MEDIUM
# 73

'''     https://leetcode.com/problems/set-matrix-zeroes/description/        '''

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.


# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """     
        # c=[0,0,0]
        # r=[0,0,0]
        m=len(matrix[0])
        n=len(matrix)
        # print(m,n)
        c=[0]*len(matrix[0])
        r=[0]*len(matrix)

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    c[j]=1
                    r[i]=1
        # print(c,r)

        for i in range(len(c)):
            if c[i]==1:
                for j in range(len(matrix)):
                    matrix[j][i]=0
        for i in range(len(r)):
            if r[i]==1:
                for j in range(len(matrix[0])):
                    matrix[i][j]=0
        return matrix
    
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))