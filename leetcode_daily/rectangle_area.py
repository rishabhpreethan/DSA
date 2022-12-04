#MEDIUM
# 223

'''     https://leetcode.com/problems/rectangle-area/    '''


# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).


# Example 1:
# Rectangle Area
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45

# Example 2:
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16


def computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    a1=(ax2-ax1)*(ay2-ay1)
    a2=(bx2-bx1)*(by2-by1)
    o1=max(min(ax2,bx2)-max(ax1,bx1),0)
    o2=max(min(ay2,by2)-max(ay1,by1),0)
    o=o1*o2
    total=a1+a2-o
    return total

print(computeArea(-3,0,3,4,0,-1,9,2))