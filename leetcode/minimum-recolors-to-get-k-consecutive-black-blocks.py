class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j, minval = 0, k, k
        while j <= len(blocks):
            count = blocks[i:j].count("W")
            minval = min(minval, count)
            i += 1
            j += 1
        return minval