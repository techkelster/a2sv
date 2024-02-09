class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u" }
        vowelCount = 0
        maxCount = 0
        low = 0

        for i in range(k):
            if s[i] in vowels:
                vowelCount += 1
        maxCount = max(maxCount, vowelCount)
        
        for r in range(k, len(s)):
            if s[r] in vowels:
                vowelCount += 1
            if s[low] in vowels:  
                vowelCount -= 1
            low += 1
            maxCount = max(maxCount, vowelCount)
        
        return maxCount
