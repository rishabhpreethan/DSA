#HARD

"""KADANE'S ALGORITHM"""

# 363
# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
# It is guaranteed that there will be a rectangle with a sum no larger than k.


# Example 1:
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# ----------------
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

# Example 2:
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3



from bisect import bisect_left, insort

def maxSumSubmatrix(matrix, k):
        m, n = len(matrix), len(matrix[0])
        res = -1000
        
        for l in range(n):
            rowSums = [0] * m
            for r in range(l, n):
                colSums = [0]
                colSum = 0
                for i in range(m):
                    rowSums[i] += matrix[i][r]
                    colSum += rowSums[i]
                    diff = colSum - k
                    idx = bisect_left(colSums, diff)
                    if idx < len(colSums):
                        if colSums[idx] == diff:
                            return k
                        else:
                            res = max(res, colSum - colSums[idx])
                    insort(colSums, colSum)
        return res

print(maxSumSubmatrix([[1,0,1],[0,-2,3]],2))