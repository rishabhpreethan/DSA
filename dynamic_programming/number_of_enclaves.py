#MEDIUM
# 1020

'''     https://leetcode.com/problems/number-of-enclaves/description/       '''

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.


# Example 1:
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# ------------------------------------------------------------------
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Example 2:
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# ------------------------------------------------------------------
# Explanation: All 1s are either on the boundary or can reach the boundary.


def numEnclaves(grid):
    row,col=len(grid),len(grid[0])
    def dfs(r,c):
        if(r<0 or c<0 or r==row or c==col or not grid[r][c] or (r,c) in visited):
            return 0
        visited.add((r,c))
        s=1
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        for x,y in d:
            s+=dfs(x+r,y+c)
        return s

    visited=set()
    mid,out=0,0
    for r in range(row):
        for c in range(col):
            mid+=grid[r][c]
            if (grid[r][c] and (r,c) not in visited and c in [0,col-1] or r in [0,row-1]):
                out+=dfs(r,c)

    return mid-out

print(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))