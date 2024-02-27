class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqDict = {}
        for char in s:
            freqDict[char] = freqDict.get(char, 0) + 1
        length = 0

        for freq in freqDict.values():
            length += freq // 2 * 2
        
        if any(freq % 2 == 1 for freq in freqDict.values()):
            length += 1
        
        return length