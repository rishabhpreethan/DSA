public class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        final int n = capacity.length;
        for (int i = 0; i < n; i++) {
        capacity[i] -= rocks[i];
        }

        Arrays.sort(capacity);
        int count = 0;
        for (int i = 0; i < n && additionalRocks > 0; i++) {
        if (additionalRocks >= capacity[i]) {
            count++;
        }
        additionalRocks -= capacity[i];
        }

        return count;
    }

    public static void main(String args[]){
        Solution obj=new Solution();
        int a[]={2,3,4,5};
        int b[]={1,2,4,4};
        System.out.println(obj.maximumBags(a,b,2));
    }
}