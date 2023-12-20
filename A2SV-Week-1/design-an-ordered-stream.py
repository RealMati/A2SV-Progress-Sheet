class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr=[0]*n
        self.ptr=0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[idKey-1]=value
        res=[]

        if idKey-1==self.ptr:
            
            while self.ptr<len(self.arr) and self.arr[self.ptr]!=0:
                res.append(self.arr[self.ptr])
                self.ptr+=1
        return res
        



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)