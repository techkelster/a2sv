class Solution:
    def largestOddNumber(self, num: str) -> str:
        end = -1
        for i in range(len(num)):
            if int(num[i]) % 2 != 0 and int(num[i] != 0):
                end = i
        if end >= 0:
            return num[:end + 1] 
        return ""
        