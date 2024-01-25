class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, diff = 0, float("inf")
        n = len(nums)
        
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(sums-target) <= diff:
                    diff = abs(sums-target)
                    ans = sums
                if sums < target:
                    j += 1
                else:
                    k -= 1
        
        return ans