class RandomizedSet:

    def __init__(self):
        self.dic={}
        self.nums=[]
        self.sett=set()

    def insert(self, val: int) -> bool:
        if val in self.sett: return False
        self.sett.add(val)
        self.nums.append(val)
        self.dic[val]=len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.sett: return False

        last=self.nums[-1]
        self.nums[self.dic[val]], self.nums[-1] = self.nums[-1], self.nums[self.dic[val]]
        
        self.sett.remove(val)
        self.dic[last]=self.dic[val]
        del self.dic[val]
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()