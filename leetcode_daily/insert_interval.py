#MEDIUM
# 57

'''     https://leetcode.com/problems/insert-interval/description/      '''

# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.


# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# --------------------------------------------------------------------------------------
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


def insert(intervals, newInterval):
    def binary_search(x,n):
        s=0
        e=len(x)-1
        while s<=e:
            mid=(s+e)//2
            if x[mid]==n:
                return mid
            elif x[mid]<n:
                s=mid+1
            else:
                e=mid-1
        return e+1
    if not intervals:
        intervals.append(newInterval)
        return intervals
    x=[]
    for i in range(len(intervals)):
        x.append(intervals[i][1])
    k=binary_search(x,newInterval[0])
    res=intervals[:k]
    while k<len(intervals) and intervals[k][0]<=newInterval[1]:
        newInterval[0]=min(intervals[k][0],newInterval[0])
        newInterval[1]=max(intervals[k][1],newInterval[1])
        k+=1
    res.append(newInterval)
    res+=intervals[k:]  
    return res

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))