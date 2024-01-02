class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W|_', '', s).lower()

        j  = len(s) - 1
        for i in s:
            if i != s[j]:
                return False
            j = j - 1
        return True
        