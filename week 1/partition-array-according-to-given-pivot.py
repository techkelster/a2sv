class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        equla = []

        for i in range(len(nums)):
            if nums[i] > pivot:
                great.append(nums[i])
            elif nums[i] < pivot:
                less.append(nums[i])
            else:
                equla.append(nums[i])
        return less  + equla + great
        