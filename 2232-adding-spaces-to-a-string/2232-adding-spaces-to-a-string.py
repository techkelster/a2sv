class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s_mod = ''
        j = 0
        for i in range(len(spaces)):
            s_mod += s[:spaces[i] - j] + " "
            s = s[spaces[i] - j:]
            j = spaces[i]
        return s_mod + s
            
            
        