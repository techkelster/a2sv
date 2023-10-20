class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        ans = []
        temp_dic = {}
        for i in range(len(temp)):
            if temp[i] not in temp_dic:
                temp_dic[temp[i]] = i
        for i in range(len(nums)):
            ans.append(temp_dic[nums[i]])
        return ans

        