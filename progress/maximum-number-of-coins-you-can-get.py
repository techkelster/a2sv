class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        theSum = 0
        print(piles)
        for i in range(len(piles) // 3, len(piles), 2):
            print(piles[i])
            theSum += piles[i]
        return theSum

        