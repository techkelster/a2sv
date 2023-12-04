class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i = 0
        while i < (min(len(word1), len(word2))):
            ans += (word1[i] + word2[i])
            i += 1
        if len(word1) > len(word2):
            ans += word1[i:len(word1)]
        else:
            ans += word2[i:len(word2)]
        return ans
        