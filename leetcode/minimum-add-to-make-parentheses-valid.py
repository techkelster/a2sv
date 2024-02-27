class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        for par in s:
            if par == ")":
                if st and st[-1] == "(":
                    st.pop()
                    continue
            st.append(par)
        return len(st)