class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []

        def generator(openp , closep) :
            if openp == closep == n :
                ans.append("".join(stack))
                return

            if openp <  n :
                stack.append("(")
                generator(openp + 1 , closep)
                stack.pop()

            if closep < openp :
                stack.append(")")
                generator(openp , closep+1)
                stack.pop()

        generator(0 , 0)
        return ans                


        