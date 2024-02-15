from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cur = []
        for bill in bills:
            if bill == 5:
                cur.append(bill)
            elif bill == 10:
                if 5 in cur:
                    cur.remove(5)
                else:
                    return False
                cur.append(bill)
            elif bill == 20:
                if 10 in cur and 5 in cur:
                    cur.remove(10)
                    cur.remove(5)
                elif cur.count(5) >= 3:
                    cur.remove(5)
                    cur.remove(5)
                    cur.remove(5)
                else:
                    return False
                cur.append(bill)
        return True
