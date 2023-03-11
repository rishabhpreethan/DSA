#MEDIUM
# 994

'''     https://leetcode.com/problems/rotting-oranges/description/      '''

# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# ----------------------------------------------------------
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# ----------------------------------------------------------
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.



from collections import deque

def orangesRotting(grid):
    q=deque()
    fresh=0
    time=0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                fresh+=1
            if grid[r][c]==2:
                q.append((r,c))

    directions=[[0,1],[0,-1],[1,0],[-1,0]]
    while fresh>0 and q:
        length=len(q)
        for i in range(length):
            r,c=q.popleft()
            for dr,dc in directions:
                row,col=r+dr,c+dc
                if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                    grid[row][col]=2
                    q.append((row,col))
                    fresh-=1
        time+=1
    if fresh==0:
        return time
    else:
        return -1
    
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))