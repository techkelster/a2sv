class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        has={0:1}
        ans=0
        theSum=0
        for i in nums:
            theSum+=i
            ans+=has.get(theSum - goal,0)
            has[theSum]=has.get(theSum,0)+1
        return ans