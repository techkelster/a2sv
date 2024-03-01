class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        size = len(nums)
        end = nums[size - 1]
        operations = 0
        
        for i in range(size - 2, -1, -1):
            if nums[i] > end:
                times = nums[i] // end
                if nums[i] % end:
                    times += 1
                end = nums[i] // times
                operations += times - 1
            else:
                end = nums[i]
        return operations
                    

                

