class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            i += 1
        for j in nums:
            if j != 0:
                ans.append(j)
        return ans + (len(nums) - (len(ans))) * [0]

        
        