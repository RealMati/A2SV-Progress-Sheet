class Bitset:

    def __init__(self, size: int):
        self.dic=defaultdict(int) 
        self.ones=0
        self.zero=size
        self.flips=0
        self.size=size

    def fix(self, idx: int) -> None:
        if self.flips%2==1:
            if self.dic[idx]==1: 
                self.dic[idx]=0
                self.ones+=1
                self.zero-=1
        else:
            if self.dic[idx]==0:
                self.dic[idx]=1
                self.ones+=1
                self.zero-=1

    def unfix(self, idx: int) -> None:
        if self.flips%2==0:
            if self.dic[idx]==1: 
                self.dic[idx]=0
                self.ones-=1
                self.zero+=1
        else:
            if self.dic[idx]==0:
                self.dic[idx]=1
                self.ones-=1
                self.zero+=1

    def flip(self) -> None:
        self.flips+=1
        self.ones, self.zero = self.zero, self.ones

    def all(self) -> bool:
        return self.ones==self.size

    def one(self) -> bool:
        return self.ones
    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        res=[]
        # print(self.dic,self.flips)
        
        if self.flips%2==1:
            for idx in range(self.size):
                res.append(str(abs(self.dic[idx]-1)))
        else:
            for idx in range(self.size):
                res.append(str(self.dic[idx]))
        return "".join(res)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()