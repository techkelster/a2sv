class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        j = len(nums) - 1
        i = 0
        k = len(nums) - 1
        while i < j:
            if nums[i] ** 2 == nums[j] ** 2:
                ans[k], ans[k - 1] = nums[i] ** 2, nums[j] ** 2
                i += 1
                j -= 1
                k -= 2
            elif nums[i] ** 2 > nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1
                k -= 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
                k -= 1
        if k == 0:
            ans[k] = nums[i] ** 2
        return ans