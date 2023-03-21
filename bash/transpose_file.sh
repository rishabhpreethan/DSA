#MEDIUM
# 194

'''     https://leetcode.com/problems/transpose-file/description/       '''

# Given a text file file.txt, transpose its content.
# You may assume that each row has the same number of columns, and each field is separated by the ' ' character.


# Example:

# If file.txt has the following content:
# name age
# alice 21
# ryan 30

# Output the following:
# name alice ryan
# age 21 30



#!bin/bash

i=1
c=$(cat file.txt | head -n 1 | wc -w)
while [ $i -le $c ]
do
    cat file.txt | cut -d ' ' -f $i | tr '\n' ' ' | rev | cut -c2- | rev
    let i=i+1
done

exit 0