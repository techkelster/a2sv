class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        leftCards = size - k
        totalSum = sum(cardPoints)
        windowSum = sum(cardPoints[:leftCards])
        minSum = windowSum

        for i in range(leftCards, size):
            windowSum = windowSum - cardPoints[i - leftCards] + cardPoints[i]
            minSum = min(windowSum, minSum)
        return totalSum - minSum
        