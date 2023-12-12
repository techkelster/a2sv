class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        the_sum = sum([x for x in nums if x % 2 == 0])
        for i in queries:
            temp = nums[i[1]]
            nums[i[1]] = nums[i[1]] + i[0]
            if nums[i[1]] % 2 == 0 and temp % 2 == 0:
                the_sum -= temp
                the_sum += nums[i[1]]
            elif nums[i[1]] % 2 == 0:
                the_sum += nums[i[1]]
            else:
                if temp % 2 == 0:
                    the_sum -= temp
            ans.append(the_sum)
        return ans
        