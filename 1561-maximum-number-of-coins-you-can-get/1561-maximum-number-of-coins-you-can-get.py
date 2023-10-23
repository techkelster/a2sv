class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_sum = 0 
        for i in range(len(piles)//3, len(piles), 2):
            max_sum += piles[i]

        return max_sum