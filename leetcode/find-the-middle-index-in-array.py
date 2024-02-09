class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums) + 1)
        suffix = []
        totalSum = sum(nums)
        for i in range(1, len(nums) + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        for i in range(len(nums)):
            suffix.append(totalSum)
            totalSum -= nums[i]
        suffix.append(totalSum)
        # print(suffix, "./n", prefixSum)
        for i in range(len(suffix) - 1):
            if suffix[i + 1] == prefixSum[i]:
                return i
        return -1


        