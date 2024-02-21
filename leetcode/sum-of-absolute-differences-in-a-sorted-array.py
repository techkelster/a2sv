class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
       preSum = [0] * (len(nums) + 1)
       sufSum = [0] * (len(nums) + 1)
       ans = []
       for i in range(1, len(nums) + 1):
           preSum[i] = preSum[i - 1] + nums[i - 1]
       totalSum = sum(nums)
       sufSum[0] = totalSum
       for i in range(1, len(nums) + 1):
           sufSum[i] = sufSum[i - 1] - nums[i - 1]
       for i in range(len(nums)):
           if i == 0:
               ans.append(abs(sufSum[i + 1] - nums[i] * (len(nums) - (i + 1))))
           else:
               ans.append(abs((sufSum[i + 1] - nums[i] * (len(nums) - (i + 1))) + abs(preSum[i] - (nums[i] * (i)))))
       print(sufSum, 'sufSum')
       print(preSum, 'preSum')
       return ans
        

        
        