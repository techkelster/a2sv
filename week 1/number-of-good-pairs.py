class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pair_count += 1
        return good_pair_count
                    
                
        