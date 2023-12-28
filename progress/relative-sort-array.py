class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        nums_dict = {}
        ans = []
        for j in arr2:
            nums_dict[j] = 0
        for i in arr1:
            if i in nums_dict:
                nums_dict[i] += 1
        for k in nums_dict:
            ans += [k] * nums_dict[k]
        arr1.sort()
        return ans + [x for x in arr1 if x not in nums_dict]

        