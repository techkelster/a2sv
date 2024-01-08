class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        right = len(people) - 1
        left = 0
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
                left += 1
            else:
                right -= 1
            boats += 1
        return boats
        