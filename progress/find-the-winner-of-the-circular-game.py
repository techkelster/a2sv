class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        frds = list(range(1, n + 1))
        j = k
        while len(frds) != 1:
            # Adjust j to stay within the bounds of the list
            j = (j - 1) % len(frds)
            frds.pop(j)
            j += k
        return frds[0]

        