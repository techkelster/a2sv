class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        ans = []
        part = len(nums) / 3
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        for i in nums_dict.keys():
            if nums_dict[i] > part:
                ans.append(i)
        return ans
                
            
        