class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        theMax = window_sum
        print(window_sum)
        for i in range(k, len(nums)):
            print(window_sum)
            window_sum -= nums[i - k]
            window_sum += nums[i]
            theMax = max(theMax, window_sum) 

        return theMax / k
        