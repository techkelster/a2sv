class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                i = j + 1
                while i < len(nums) and nums[i] == 0:
                    i += 1
                if i < len(nums):
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
            else:
                j += 1
                
            
                
            