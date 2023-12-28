class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_dict = {}
        ans = []
        un_nums = set(nums1) & set(nums2)
        for i in un_nums:
            nums_dict[i] = [0, 0]
       
        for j in nums1:
            if j in nums_dict:
                nums_dict[j][0] += 1

        for z in nums2:
            if z in nums_dict:
                nums_dict[z][1] += 1
        print(nums_dict)
        for k in nums_dict:
            ans += [k] * min(nums_dict[k][0], nums_dict[k][1])
        return ans
        