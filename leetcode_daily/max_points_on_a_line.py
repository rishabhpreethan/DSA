#HARD
# 149

'''     https://leetcode.com/problems/max-points-on-a-line/description/     '''

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.


# Example 1:
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4


from cmath import inf
from collections import defaultdict

def maxPoints(points):
    if len(points)<=2:
        return len(points)

    def line(p1,p2):
        if p2[0]-p1[0] == 0:
            return inf
        return (p2[1]-p1[1]) / (p2[0]-p1[0])    

    mx = 0
    for i in range(len(points)):
        c = defaultdict(int)
        for j in range(i+1,len(points)):
            c[line(points[i],points[j])] += 1
        if c:
            mx = max(mx,max(c.values()))
    
    return mx + 1

print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))