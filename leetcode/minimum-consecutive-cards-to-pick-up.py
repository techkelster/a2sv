class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        nums_set = {}
        for r in range(len(cards)): 
            if cards[r]  in nums_set: 
                res = min(res, r-nums_set[cards[r]]+1)
            nums_set[cards[r]] = r
            
        return res if res != float("inf") else -1