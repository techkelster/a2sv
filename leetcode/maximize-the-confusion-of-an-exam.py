class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        ans = 0
        i = l = cnt = 0
        
        while i < len(s):
            if s[i] == 'T':
                cnt += 1
            
            while cnt > k:
                if s[l] == 'T':
                    cnt -= 1
                
                l += 1
            
            ans = max(ans, i - l + 1)
            i += 1
        
        cnt = l = i = 0
        while i < len(s):
            if s[i] == 'F':
                cnt += 1
            
            while cnt > k:
                if s[l] == 'F':
                    cnt -= 1
                
                l += 1
            
            ans = max(ans, i - l + 1)
            i += 1
        
        return ans
