class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        path_one = sum(distance[start: destination])
        path_two = sum(distance[destination:]) + sum(distance[:start])
        
        return min(path_one, path_two)
        