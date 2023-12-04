class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_ref = {
            "0":0,
            "1":1,
            "2":2, 
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        if "0" in [num1, num2]:
            return "0"
        
        ans = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                mult = num_ref[num1[i]] * num_ref[num2[j]]
                ans[i + j] += mult
                ans[i + j + 1] += (ans[i + j] // 10)
                ans[i + j] = ans[i + j] % 10
        ans, beg = ans[::-1], 0
        while beg < len(ans) and ans[beg] == 0:
            beg += 1
        ans = map(str, ans[beg:])
        return "".join(ans)
        