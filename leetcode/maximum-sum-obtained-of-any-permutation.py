class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7

        cntrs = [0] * len(nums)

        for start, end in requests:
            cntrs[start] += 1
            if end + 1 < len(nums):
                cntrs[end + 1] -= 1

        for i in range(1, len(cntrs)):
            cntrs[i] += cntrs[i - 1]
            
        sorted_nums = sorted(nums)
        sorted_cntrs = sorted(cntrs)
        result = sum(num * cnt for num, cnt in zip(sorted_nums, sorted_cntrs)) % MOD

        return result
