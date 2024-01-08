class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 0;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i - 1] != nums[i]) {
                j++;
                nums[j] = nums[i];
            }
        }
        return j + 1;
        
    }
}