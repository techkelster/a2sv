class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        theSum = 0
        ans = 0
        for i in range(len(nums)):
            theSum += nums[i]
            ans = max(ans, (theSum + i) // (i + 1))
        return ans