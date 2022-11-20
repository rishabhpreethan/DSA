#EASY
# 566

'''     https://leetcode.com/problems/reshape-the-matrix/    '''


# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]



def matrixReshape(mat,r,c):
    n=len(mat[0])
    m=len(mat)
    tmp=[]
    k=0
    t=r*c
    if n*m!=t: return mat
    output=[[0 for _ in range(c)] for _ in range(r)]
    for i in range(m):
        for j in range(n):
            tmp.append(mat[i][j])
            
    for i in range(r):
        for j in range(c):
            output[i][j]=tmp[k]
            k+=1
            
    return output

print(matrixReshape([[1,2],[3,4]],1,4))