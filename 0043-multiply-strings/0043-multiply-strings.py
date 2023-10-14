class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = 10 ** (len(num1) - 1)
        num_2 = 10 ** (len(num2) - 1)
        sum_1 = 0
        sum_2 = 0
        for i in num1:
            sum_1 = sum_1 + ((ord(i) - 48) * num_1 )
            num_1 = num_1 // 10
        for i in num2:
            sum_2 =  sum_2 + ((ord(i) - 48) * num_2)
            num_2 = num_2 // 10
        return str( sum_1 * sum_2)
            
            