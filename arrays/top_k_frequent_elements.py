#MEDIUM

#347
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]



# Example 2:

# Input: nums = [1], k = 1
# Output: [1]




import operator


def topKFrequent(nums, k):
    d={}
    l=[]

    #creating dictionary with key as number and value as the count of the number
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    #sorting the dictionary in descending order based on the value(i.e. count)
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

    #sorting based on keys(i.e. number)
    v=list(sorted_d.keys())


    for i in range(k):
        l.append(v[i])

    return l

print(topKFrequent([3,0,1,0],1))