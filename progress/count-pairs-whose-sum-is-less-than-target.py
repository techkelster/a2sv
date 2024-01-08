class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort() 
        pairCount = 0 
        left = 0 
        right = len(nums)-1 
        while(left < right):
            if(nums[left] + nums[right] < target):
                pairCount += right-left 
                left += 1 
            else: 
                right -= 1 
        return pairCount
