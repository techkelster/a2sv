class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        orderRef = {}
        ans = [0] * len(s)
        for i in range(len(indices)):
            orderRef[indices[i]] = s[i]
        for i in orderRef:
            ans[i] = orderRef[i]
        return "".join(ans)