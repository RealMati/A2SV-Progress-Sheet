class ATM(object):

    def __init__(self):
        self.notes=[20,50,100,200,500]
        self.noteCount={20:0, 50:0, 100:0, 200:0, 500:0}

    def deposit(self, banknotesCount):
        """
        :type banknotesCount: List[int]
        :rtype: None
        """
        for idx in range(len(banknotesCount)):
            self.noteCount[self.notes[idx]]+=banknotesCount[idx]
            


        

    def withdraw(self, amount):
        """
        :type amount: int
        :rtype: List[int]
        """
             
        res=[0]*len(self.notes)
        temp=dict(self.noteCount)
        noteidx=len(self.notes)-1

        for idx in range(len(self.notes)-1,-1,-1):
            if amount>=self.notes[idx]:
                if self.noteCount[self.notes[idx]]:
                    val=min((amount//self.notes[idx]),self.noteCount[self.notes[idx]])
                    res[idx]+=val
                    self.noteCount[self.notes[idx]]-=val
                    amount-=val*self.notes[idx]

                    
        if amount>0:
            self.noteCount=temp
            return [-1]
        return res

        # while noteidx>=0:
        #     if amount>=self.notes[noteidx]:
        #         if self.noteCount[self.notes[noteidx]]>0:
        #             self.noteCount[self.notes[noteidx]]-=1
        #             amount-=self.notes[noteidx]
        #             res[noteidx]+=1
        #         else: noteidx-=1
                
        #     else:noteidx-=1
            
        #     if noteidx==-1 and amount>0:
        #         self.noteCount=temp
        #         return [-1]            

        # return res


        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)