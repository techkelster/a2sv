class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        distancePrefix = [0] * 1001
        left = float('inf')
        right = 0
        for trip in trips:
            distancePrefix[trip[1]] += trip[0]
            distancePrefix[trip[2]] -= trip[0]
            left = min(left, trip[1])
            right = max(right, trip[2])
        
        numPassenger = 0

        for i in range(int(left), right + 1):
            numPassenger += distancePrefix[i]
            print(distancePrefix[i])
            if numPassenger > capacity: 
                return False
        return True


