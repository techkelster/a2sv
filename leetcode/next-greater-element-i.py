class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(lambda : -1)
        stack = []
        ans = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                nextGreater[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for num in nums1:
            ans.append(nextGreater[num])
        return ans