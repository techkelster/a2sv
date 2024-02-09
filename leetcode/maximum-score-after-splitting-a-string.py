class Solution:
    def maxScore(self, s: str) -> int:
        prefixSum = [0] * (len(s) + 1)
        sufix = []
        sumed = 0
        maxed = 0
        for i in range(1, len(s) + 1):
            prefixSum[i] = prefixSum[i - 1] + int(not int(s[i - 1]))
            sumed += int(s[i - 1])
        for i in range(len(s)):
            sufix.append(sumed)
            sumed -= int(s[i])
        sufix.append(sumed)
        print(prefixSum, sufix)
        for i in range(1,len(prefixSum) - 1):
            maxed = max(maxed, prefixSum[i] + sufix[i])
        return maxed

        

        