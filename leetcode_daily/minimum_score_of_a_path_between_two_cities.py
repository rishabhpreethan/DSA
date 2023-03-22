#MEDIUM
# 2492

'''     https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/       '''

# You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.

# Note:
# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1 and n.


# Example 1:
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# --------------------------------------------------------------
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.

# Example 2:
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# --------------------------------------------------------------
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.



from collections import defaultdict
import math

def minScore(n,roads):
    m=defaultdict(list)
    for a,b,dist in roads:
        m[a].append([b,dist])
        m[b].append([a,dist])
    fin=[math.inf]
    visited=set()
    def dfs(node):
        visited.add(node)
        for n,cost in m[node]:
            fin[0]=min(fin[0],cost)
            if n in visited:
                continue
            dfs(n)
    dfs(1)
    return fin[0]

print(minScore(4,[[1,2,2],[1,3,4],[3,4,7]]))