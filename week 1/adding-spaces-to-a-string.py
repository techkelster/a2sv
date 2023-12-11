class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        last = 0
        for i in spaces:
            ans += s[last:i]
            ans += ' '
            last = i
        ans += s[last:]
        return ans
        
        