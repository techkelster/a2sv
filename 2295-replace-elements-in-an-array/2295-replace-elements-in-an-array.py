class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        r_dic = {}
        for o, r in reversed(operations):
            r_dic[o] = r_dic.get(r, r)
        for i, v in enumerate(nums):
            if v in r_dic:
                nums[i] = r_dic[v]
        return nums
        
            