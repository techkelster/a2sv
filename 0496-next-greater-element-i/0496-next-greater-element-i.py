class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: 0)
        for i in range(len(nums1)):
            d[nums1[i]] = i
            
        ans = [-1] * len(nums1)
        st = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while st and cur > st[-1]:
                val = st.pop()
                idx = d[val]
                ans[idx] = cur
            if cur in d:
                st.append(cur)
            
        return ans
                
        