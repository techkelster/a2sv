class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.perimeter = 2*(width+height)-4
        self.pos = [0, 0]
        self.dir = [1, 0]
        
    def step(self, num: int) -> None:
        num %= self.perimeter
        if num == 0 and self.pos == [0, 0] and self.dir == [1, 0]: self.dir = [0, -1]
        while num: 
            if self.dir == [1, 0]: most = self.width - self.pos[0] - 1
            elif self.dir == [0, 1]: most = self.height - self.pos[1] - 1
            elif self.dir == [-1, 0]: most = self.pos[0]
            else: most = self.pos[1]
            step = min(num, most)
            self.pos = [self.pos[0] + self.dir[0]*step, self.pos[1] + self.dir[1]*step]
            if num > most: self.dir = [-self.dir[1], self.dir[0]]
            num -= step 
            
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        if self.dir == [1, 0]: return "East"
        elif self.dir == [0, 1]: return "North"
        elif self.dir == [-1, 0]: return "West"
        return "South"