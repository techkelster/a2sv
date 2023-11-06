class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        left = 0
        right = 0
        for i in nums:
            total_sum += i
        for i in range(len(nums)):
            right = total_sum - nums[i]
            if right == left:
                return i
            left += nums[i]
            total_sum -= nums[i]
        return -1