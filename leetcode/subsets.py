class Solution:
    def __init__(self):
        self.answer = []

    def backtracking(self, start, nums, subset):
        self.answer.append(subset.copy())

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtracking(i+1, nums, subset)
            subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.backtracking(0, nums, [])
        return self.answer