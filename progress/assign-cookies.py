class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        cookies = 0
        i, j = 0, 0
       
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cookies += 1
                i += 1
            j += 1
        return cookies