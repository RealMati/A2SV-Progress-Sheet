class Solution:
    def largestGoodInteger(self, num: str) -> str:
        from collections import Counter
        count=Counter(num[:3])
        res="-1"
        if len(count)==1:
            res=num[:3]
        for i in range(3,len(num)):
            count[num[i-3]]-=1
            if count[num[i-3]]==0: del count[num[i-3]]
            count[num[i]]+=1
            if len(count)==1:
                res=max(res,num[i]*3)
        if res=="-1":
            return ""
        if res:
            return res

