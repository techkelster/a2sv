class Bitset:

    def __init__(self, size: int):
        self.bit = [False for i in range(size)]
        self.bitinv = [True for i in range(size)]
        self.ones = 0
        self.zeros = size
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.bit[idx]:
            self.zeros -= 1
            self.ones += 1
        self.bit[idx] = True
        self.bitinv[idx] = False

    def unfix(self, idx: int) -> None:
        if self.bit[idx]:
            self.zeros += 1
            self.ones -= 1
        self.bit[idx] = False
        self.bitinv[idx] = True

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones
        self.bit, self.bitinv = self.bitinv, self.bit

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        ans = ''
        for bit in self.bit:
            if bit:
                ans += '1'
            else:
                ans += '0'
        return ans
