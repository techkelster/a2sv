class Solution:
    def isValid(self, s: str) -> bool:
        stackDict = {")" : "(", "}": "{", "]" : "["}
        stack = []

        for i in range(len(s)):
            if s[i] in stackDict.values():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                print(s[i])
                if stack.pop() != stackDict[s[i]]:
                    return False
        if stack:
            return False
        return True
    

