class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 1:
            return True

        currentNum = nums[0]
        for i in range(size - 1):
            if nums[i] > currentNum:
                currentNum = nums[i]
            if currentNum == 0:
                return False
            currentNum -= 1
        return True

        