class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        size = len(tickets)
        while tickets[k] > 0:
            if tickets[i % size] > 0:
                count += 1
                tickets[i % size] -= 1
            i += 1
        return count
