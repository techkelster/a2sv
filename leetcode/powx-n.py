class Solution:
    def myPow(self, x: float, n: int) -> float:
        def con(x, n):
            if n == 0:
                return 1
            else:
                return x *  self.myPow(x * x, ((n - 1) // 2)) if n % 2 != 0 else self.myPow(x * x, (n // 2)) 
        ans = con(x, abs(n))
        return float(ans) if n >= 0 else 1/ans
        
    
        