class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        prefix_sum_count = {0: 1} 

        for num in nums:
            running_sum += num
            count += prefix_sum_count.get(running_sum - k, 0)
            prefix_sum_count[running_sum] = prefix_sum_count.get(running_sum, 0) + 1
        return count
