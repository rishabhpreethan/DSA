#MEDIUM

#128
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

 
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9



def longestConsecutive(nums):
        s=set(nums)
        longest=0
        for i in nums:

            #checking if previous number is present
            if i-1 not in s:
                length=0

                #if next number is present then length is incremented
                while i+length in s:
                    length+=1
                
                #longest stores the biggest length
                longest=max(length,longest)
        return longest

print(longestConsecutive([100,4,200,1,3,2]))


#LONGEST LIST FROM THIS IS:  [1,2,3,4]
#LENGTH IS: 4