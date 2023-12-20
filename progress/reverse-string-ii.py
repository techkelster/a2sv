class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []
        for i in range(0, len(s), 2 * k):
            ans += list(reversed(list(s[i:i + k]))) + list(s[i + k: i + 2 * k])
        return ''.join(ans)
