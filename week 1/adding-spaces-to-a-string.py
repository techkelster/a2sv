class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = s
        j = 0
        for i in spaces:
            ans = ans[:i + j] + ' ' + ans[i + j:]
            j += 1
        return ans
        
        