class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            val = [nums[i + 1]] * nums[i]
            i += 2
            ans += val
        return ans
            
            
        