class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        size = len(nums)
        ans = [-1] * size

        for i in range((2 * size) - 1, -1, -1):
            while stack and nums[i % size] >= stack[-1]:
                stack.pop()

            if stack:
                ans[i % size] = stack[-1]

            stack.append(nums[i % size])

        return ans
