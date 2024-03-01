class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        st = []
        left = [-1] * size
        right = [size] * size

        for i in range(size):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st = []
        for i in range(size - 1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
       
        result = sum([(arr[i] * (i - left[i]) * (right[i] - i)) for i in range(size)])
        
        return result % (10**9 + 7 )

        