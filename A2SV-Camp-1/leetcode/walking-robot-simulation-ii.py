class Robot:

    def __init__(self, width: int, height: int):
        self.mod=(width+height)*2 - 4
        self.w=width
        self.h=height
        self.pos=0
        self.moved=False
        
    def step(self, num: int) -> None:
        self.pos= (self.pos + num) % self.mod
        self.moved=True

    def getPos(self) -> List[int]:
        # print(self.pos)
        if 0<=self.pos<=self.w-1:
            return [self.pos, 0]
        if self.w<=self.pos<=self.w+self.h-2:
            return [self.w-1, self.pos-self.w+1]
        if self.w+self.h-2<=self.pos<=self.w*2+ self.h -3:
            return [(self.w*2+ self.h -3)-self.pos, self.h-1]
        if self.w*2+ self.h -3<=self.pos<=self.w*2+self.h*2-4:
            return [0, self.w*2+self.h*2-4-self.pos]

    def getDir(self) -> str:
        # print(self.pos)
        if self.moved and self.pos==0: return "South"
        if not self.moved and self.pos==0: return "East"
        if 0<self.pos<=self.w-1:
            return "East"
        if self.w-1<=self.pos<=self.w+self.h-2:
            return "North"
        if self.w+self.h-1<=self.pos<=self.w*2+ self.h -3:
            return "West"
        if self.w*2+ self.h - 3<=self.pos<=self.w*2+self.h*2-4:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()