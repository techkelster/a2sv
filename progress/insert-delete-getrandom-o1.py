class RandomizedSet:

    def __init__(self):
        self.elem_dict = {}
        self.elem_list = []

    def insert(self, val: int) -> bool:
        if val in self.elem_dict:
            return False
        self.elem_dict[val] = len(self.elem_list)
        self.elem_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.elem_dict:
            last_elem = self.elem_list[-1]
            index_to_remove = self.elem_dict[val]

            self.elem_dict[last_elem] =  index_to_remove
            self.elem_list[index_to_remove] = last_elem
            self.elem_list[-1] = val
            self.elem_list.pop()
            self.elem_dict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.elem_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()