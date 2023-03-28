#MEDIUM
# 64

'''     https://leetcode.com/problems/minimum-path-sum/     '''

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7

# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12


m=pow(2,31)-1
def minPathSum(self,grid):
    n=len(grid)
    m=len(grid[0])
    d=[[1,0],[0,1]]
    dp=[[self.m for _ in range(0,m)] for _ in range(0,n)]
    dp[n-1][m-1]=grid[n-1][m-1]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            for dir in d:
                x=i+dir[0]
                y=j+dir[1]
                if(x<n and y<m ):
                    dp[i][j]=min( dp[i][j],dp[x][y]+grid[i][j])

    return dp[0][0]