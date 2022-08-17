nums=[1,2,3,1]

#making set of nums to get rid duplicates 
s=set(nums)

#if length of nums = length of the set print false
if len(s)==len(nums):
    print('False')
else:
    print('True')