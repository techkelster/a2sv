class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        st = []
        mini2 = float('-inf')

        for i in range(n-1,-1,-1):
            if i==n-1:
                st.append(nums[i])
            if nums[i] < mini2:
                return True
            if nums[i]<st[-1] :
                st.append(nums[i])
            elif nums[i]>st[-1] :
                while(len(st)>0 and nums[i] > st[-1]) :
                    mini2 = st[-1]
                    st.pop()                    
                st.append(nums[i])

        return False

        