class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        the_incremeted = int("".join(list(map(str, digits)))) + 1
        for i in str(the_incremeted):
            ans.append(int(i))
        return ans