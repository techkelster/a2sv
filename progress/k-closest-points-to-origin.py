class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceCalc(x):
            return (x[0] ** 2 + x[1] ** 2) ** 0.5
        points.sort(key = distanceCalc)
        return points[0:k]


        