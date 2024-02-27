class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        k = n-1
        ans = 0
        while k >= 2:
            i, j = 0, k-1
            while i < j:
                if nums[i]+nums[j] > nums[k]:
                    ans += (j-i)
                    j -= 1
                else:
                    i += 1
            k -= 1
        return ans