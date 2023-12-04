class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                max_ones = max(max_ones, temp)
                temp = 0
        max_ones = max(max_ones, temp)
        return max_ones