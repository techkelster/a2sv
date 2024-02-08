class Solution:
    def bestClosingTime(self, customers: str) -> int:
        total = Counter(customers)
        n = 0
        y = total['Y']
        penalty = len(customers) + 1
        index = 0

        for i in range(len(customers)):
            if penalty > n + y:
                penalty = n + y
                index = i
                
            if customers[i] == 'N':
                n += 1
            else:
                y -= 1
        if penalty > n + y:
            penalty = n + y
            index = len(customers)

        return index