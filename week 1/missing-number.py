class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        the_sum = ((len(nums)) * (len(nums) + 1))/2
        for i in nums:
            the_sum -= i 
        return int(the_sum)

        