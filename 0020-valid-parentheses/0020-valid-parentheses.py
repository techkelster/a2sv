class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {
            '(' : ")",
            '{' : '}',
            '[' : ']'
        }
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            elif len(stack) == 0 or i != open_close[stack.pop()]:
                return False
        return len(stack) == 0
                
        
        