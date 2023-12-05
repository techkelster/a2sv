class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = 1
        steps = 1
        temp = capacity
        capacity = capacity - plants[0]
        while i < len(plants):
            if capacity >= plants[i]:
                steps += 1
                capacity -= plants[i]
                i += 1
            else: 
                steps += (2 * (i)) 
                capacity = temp
        return steps
            
        