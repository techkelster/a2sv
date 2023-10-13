class Solution:
    def reverse(self, x: int) -> int:
        sum_n = 0
        flag  = False
        if x < 0:
            flag = True
            x = abs(x)
        while x != 0:
            last_digit = x % 10
            x = x // 10
            sum_n = (sum_n * 10) + last_digit
        if flag:
            sum_n = -sum_n
        if sum_n <= -2 ** 31 or sum_n >= 2 ** 31 -1:
            return 0
        return sum_n
            