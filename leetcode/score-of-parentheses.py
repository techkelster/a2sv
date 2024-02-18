class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        start = 0
        balance = 0
        for i, p in enumerate(S):
            if p == '(':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                inside = self.scoreOfParentheses(S[start+1:i])
                if inside == 0:
                    ans += 1
                else:
                    ans += 2 * inside
                start = i + 1
        return ans
            