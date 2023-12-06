class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * n * 2
        j = n
        k = 0
        i = 0
        while i < (2 * n):
            ans[i] = nums[k]
            i += 1
            ans[i] = nums[j] 
            k += 1
            j += 1
            i += 1
        return ans
        