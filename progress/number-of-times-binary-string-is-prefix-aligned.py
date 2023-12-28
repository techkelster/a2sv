class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        flipEnd = flips[0]
        counter = 0
        for i, j in enumerate(flips):
            flipEnd = max(flipEnd, j)
            if (i + 1) == flipEnd:
                counter += 1
        return counter
        

        