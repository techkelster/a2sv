class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        counter = 0
        ans = ""
        for i in s:
            if i == "(":
                counter += 1
                st.append(i)
            else:
                counter -= 1
                st.append(i)
            if counter == 0:
                ans += "".join(st[1:-1])
                st = []
        return ans
                
                
        
        