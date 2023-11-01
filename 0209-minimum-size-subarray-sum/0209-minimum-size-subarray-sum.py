class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        size = len(nums)
        ans = size + 1
        
        for i in range(size):
            sum_ += nums[i]
            while sum_ >= target:
                ans = min(ans, i + 1 - left)
                sum_ -= nums[left]
                left += 1
        return  ans if ans != size + 1 else 0