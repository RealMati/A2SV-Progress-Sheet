class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curSum=customers.count("Y")
        minimum=customers.count("Y") #
        res=-1
        if curSum==0: return 0
        for idx,ch in enumerate(customers):
            if ch=="Y": curSum-=1
            else: curSum+=1

            if minimum>curSum:
                minimum=curSum
                res=idx

        return res+1

        
