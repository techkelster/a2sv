class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        preProduct = 1
        for i in range(len(nums)):
            ans[i] *= preProduct
            preProduct *= nums[i]

        sufProduct = 1
        for i in range(len(nums)  - 1, -1, -1):
            ans[i] *= sufProduct
            sufProduct *= nums[i]
        return ans

        
        