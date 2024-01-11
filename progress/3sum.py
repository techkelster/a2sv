class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        
        for i in range(len(nums) - 2):
            # Avoid duplicate values for the first element in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                the_sum = nums[i] + nums[l] + nums[r]
                if the_sum > 0:
                    r -= 1
                elif the_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    # Avoid duplicate values for the second element in the triplet
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Avoid duplicate values for the third element in the triplet
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return ans
