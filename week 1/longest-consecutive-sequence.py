class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 0
        maxlen = 0
        while i < len(nums):
            the_num =  nums.pop()
            large = the_num + 1
            while large in nums:
                nums.remove(large)
                large += 1
            little = the_num - 1
            while little in nums:
                nums.remove(little)
                little -= 1
            maxlen = max(maxlen, large - little - 1)
        return maxlen
                


        