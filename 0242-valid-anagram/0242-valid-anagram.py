class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        freq = [0] * 26
        for i in s:
            freq[ord(i) - 97] += 1
        for i in t:
            freq[ord(i) - 97] -= 1
        for i in freq:
            if i != 0:
                return False
        return True
