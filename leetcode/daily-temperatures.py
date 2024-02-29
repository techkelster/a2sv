class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        size = len(t)
        if size == 1: return [0]
        ans = [0] * size
        st = [size - 1]
        for i in range(size-2, -1, -1):
            while st and t[i]>=t[st[-1]]:
                st.pop()
            if st:
                ans[i]=st[-1]-i
            st.append(i)
        return ans
        