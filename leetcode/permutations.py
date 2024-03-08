class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(l, p, n, ret):
            if n==0:
                ret.append(copy.deepcopy(p))
            for i in range(len(l)):
                p.append(l[i])
                temp = l.pop(i)
                ret = backtrack(l, p, n-1, ret)
                l.insert(i, temp)
                p.pop(-1)
            return ret
        ret = []
        p = []
        ret = backtrack(nums, p, len(nums), ret)

        return ret