class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        size = len(nums)
        
        for i in range(size):
            comp = target - nums[i]
            if comp in num_dic:
                return [num_dic[comp], i]
            num_dic[nums[i]] = i