class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        theMax = 0
        if coins - costs[0] >= 0:
            theMax +=  1
            coins -= costs[0]
        else:
            return theMax
        for i in range(1, len(costs)):
            if coins - costs[i] >= 0:
                theMax += 1
                coins -= costs[i]
            else:
                return theMax
        return theMax

            
        