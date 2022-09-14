//EASY

//485
//Given a binary array nums, return the maximum number of consecutive 1's in the array.
//
//Example 1:
//Input: nums = [1,1,0,1,1,1]
//Output: 3
////---------------------------------------------------
//Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
//
//Example 2:
//Input: nums = [1,0,1,1,0,1]
//Output: 2



public class max_consecutive_ones {
    public static int findMaxConsecutiveOnes(int[] nums) {
        int max=0;
        int s=0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]==1){
                s+=1;
            }
            else{
                s=0;
            }
            if (s>max){
                max=s;
            }
        }
        return max;
    }

    public static void main(String args[]){
        int nums[]={1,1,0,1,1,1};
        System.out.print(findMaxConsecutiveOnes(nums));
    }
}

