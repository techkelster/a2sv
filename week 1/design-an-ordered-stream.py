class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.values = [0] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey - 1] = value
        temp = []
        if self.values[self.ptr] != 0:
            while self.ptr < len(self.values) and self.values[self.ptr] != 0:
                temp.append(self.values[self.ptr])
                self.ptr += 1
        return temp

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)