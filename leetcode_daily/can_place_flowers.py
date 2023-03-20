#EASY
# 605

'''     https://leetcode.com/problems/can-place-flowers/description/        '''

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.


# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


def canPlaceFlowers(flowerbed,n):
    if n==0:
        return True
    flowerbed.append(0)
    flowerbed=[0]+flowerbed
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            n-=1
    return n<=0


print(canPlaceFlowers([1,0,0,0,1],1))