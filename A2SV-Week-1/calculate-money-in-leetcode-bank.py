class Solution:
    def totalMoney(self, n: int) -> int:
            
        sum_dic={0:0,1:1,2:3,3:6,4:10,5:15,6:21}
        ans=0
        for i in range(n//7):
            ans+= (i*7)+28

        ans+=(((n//7)*(n%7))+sum_dic[n%7])
        return ans



        