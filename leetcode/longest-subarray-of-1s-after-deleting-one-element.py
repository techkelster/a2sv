class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 1
        low = 0
        for end in range(len(nums)):
            zeroCount -= nums[end] == 0
            
            if zeroCount < 0:
                zeroCount += nums[low] == 0
                low += 1
        return end - low


        