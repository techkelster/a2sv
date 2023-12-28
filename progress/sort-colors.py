class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in nums:
            count[i] += 1
        for j in range(1, len(count)):
            count[j] = count[j] + count[j - 1]
        for l in range(len(count)):
            count[l] -= 1
        nums_r = [0] * len(nums)
        for k in range(len(nums) - 1, -1, -1):
            nums_r[count[nums[k]]] = nums[k]
            count[nums[k]] -= 1
        for m in range(len(nums_r)):
            nums[m] = nums_r[m]
        
        