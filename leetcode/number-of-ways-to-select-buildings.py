class Solution:
    def numberOfWays(self, s: str) -> int:
        # 001101, 
        zeros = s.count('0')
        ones = len(s) - zeros

        onZeros = 0
        onOnes = 0
        ways =  0

        for ch in s:
            if ch == '0':
                ways += onOnes * (ones - onOnes)
                onZeros += 1
            else:
                ways += onZeros * (zeros - onZeros)
                onOnes += 1
        return ways

                
                

        