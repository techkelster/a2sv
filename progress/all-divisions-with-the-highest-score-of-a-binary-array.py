class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # indexScore = {}
        # ans = []
        # def count(toCount, arr):
        #     counted = 0
        #     for i in arr:
        #         if i == toCount:
        #             counted += 1
        #     return counted
        # indexScore[0] = count(0, []) + count(1, nums) 
        # theMax = indexScore[0]
        # for i in range(1, len(nums) + 1):
        #     indexScore[i] = count(0, nums[:i]) + count(1, nums[i:]) 
        #     theMax = max(theMax, indexScore[i])
        # for i in indexScore:
        #     if indexScore[i] == theMax:
        #         ans.append(i)
        # return ans
        count_ones = 0
        for num in nums:
            if num == 1:
                count_ones += 1

        count_zeros, max_division = 0, count_ones
        index_dict = collections.defaultdict(list)
        index_dict[count_ones].append(0)

        for i, num in enumerate(nums):
            count_zeros += int(num == 0)
            count_ones -= int(num == 1)
            current_sum = count_zeros + count_ones
            index_dict[current_sum].append(i + 1)
            max_division = max(max_division, current_sum)

        return index_dict[max_division]

        

        