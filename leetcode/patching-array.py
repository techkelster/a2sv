class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        satTill = 0
        count = 0
        i = 0

        while satTill < n:
            if i < len(nums) and nums[i] <= satTill + 1:
                satTill += nums[i]
                i += 1
            else:
                satTill += satTill + 1
                count += 1

        return count
