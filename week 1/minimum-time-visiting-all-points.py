class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            optimal_second = max(abs(points[i + 1][1] - points[i][1]), abs(points[i + 1][0] - points[i][0]))
            ans += optimal_second
        return ans
                
        