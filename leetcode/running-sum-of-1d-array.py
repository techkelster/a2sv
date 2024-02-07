class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        preSum = 0
        for i in nums:
            preSum += i
            ans.append(preSum)
        return ans