class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = []
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good_integers.append(int(num[i] * 3))
                i += 2
        if good_integers:
            ans = max(good_integers)
            if ans == 0:
                return "000"
            else:
                return str(ans)
        else:
            return ""
                
            
            
            
        