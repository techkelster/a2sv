class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                j += 1
                continue
            elif j < len(nums):
                while nums[j] == 0 and j < len(nums) - 1:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        