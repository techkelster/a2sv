class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            sum = 0
            while num > 0:
                r = num % 10
                sum += r**2
                num = num // 10
            return sum
        for i in range(70):
            n = sqr(n)
            if n == 1:
                return True
        return False