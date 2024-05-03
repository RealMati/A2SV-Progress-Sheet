# Problem:  Add Binary - https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aa=bb=0
        for i in range(len(a)):
            if a[i]=="1":
                aa+=2**(len(a)-1-i)
        for i in range(len(b)):
            if b[i]=="1":
                bb+=2**(len(b)-1-i)
                # print("b",i)
              
        aa+=bb
        res=[]
        # print(aa, bb)
        while aa:
           res.append("1" if aa%2 else "0")
           aa//=2
        res=res[::-1]
        return "".join(res) if res else "0"
        
        