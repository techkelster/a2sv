class Solution:
    def sortSentence(self, s: str) -> str:
        ans = []
        m = s.split()
        m.sort(key=lambda x: int(x[-1]))
        
        for i in m:
            print(i)
            ans.append(i[:len(i) -1])
        return ' '.join(ans)
        
        