#MEDIUM

# 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


def rotate(matrix):
        n = len(matrix)
        row = 0
        col = 0
        for i in range(n//2):
            col_boundary = n - col - 1
            while col < col_boundary:
                matrix[row][col], matrix[col][n-1-row] = matrix[col][n-1-row], matrix[row][col]
                matrix[row][col], matrix[n-1-row][n-1-col] = matrix[n-1-row][n-1-col], matrix[row][col]
                matrix[row][col], matrix[n-1-col][row]  = matrix[n-1-col][row], matrix[row][col]
                col += 1
            row += 1
            col = row
        return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))