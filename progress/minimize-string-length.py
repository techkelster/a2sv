class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s = Counter(s)
        count = 0
        for k in s:
            count += 1
        return count



        