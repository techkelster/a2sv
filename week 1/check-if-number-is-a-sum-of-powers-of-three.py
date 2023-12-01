class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        the_sum = 0
        i = 16
        while i >= 0:
            if (the_sum + 3 ** i) < n:
                the_sum += 3 ** i
            elif the_sum + 3 ** i == n: return True
            i -= 1
        return False
            
            
        