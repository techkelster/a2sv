class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        nums_to_idx = collections.defaultdict(list)
        for i, n in enumerate(nums):
            nums_to_idx[n].append(i)
        
        res = [0] * len(nums)
        for n in nums_to_idx:
            l = nums_to_idx[n]
            pre = [0]
            for x in l:
                pre.append(pre[-1] + x)
            for i, x in enumerate(l):
                left = x * (i + 1) - pre[i + 1]
                right = pre[-1] - pre[i] - x * (len(l) - i)
                res[x] = left + right
        
        return res
            