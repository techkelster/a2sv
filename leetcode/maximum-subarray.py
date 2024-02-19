class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        theSum = 0
        theMax = float('-inf')
        for i in range(len(nums)):
            theSum += nums[i]
            theMax = max(theSum, theMax)
            if theSum < 0:
                theSum = 0
        return theMax

        