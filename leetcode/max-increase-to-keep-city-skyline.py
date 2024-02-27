class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        size = len(grid)
        c = []
        r = []
        for i in range(size):
            theMax = 0
            for j in range(size):
                if grid[j][i] > theMax:
                    theMax = grid[j][i]
            c.append(theMax)

        for i in range(size):
            theMax = max(grid[i])
            r.append(theMax)

        ans = 0

        for i in range(size):
            for j in range(size):
                if grid[i][j] < min(c[j], r[i]):
                    ans += min(c[j], r[i]) - grid[i][j]
        return ans



        