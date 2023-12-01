class Solution:
    def interpret(self, command: str) -> str:
        pair = {
            "G": "G",
            "()": "o",
            "(al)": "al"
        }
        
        val = ""
        ans = ""
        for i in command:
            val += i
            if val in pair:
                ans += pair[val]
                val = ""
        return ans
                
        