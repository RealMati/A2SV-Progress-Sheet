class Solution:
    def smallestNumber(self, num: int) -> int:
        s=[]
        s.extend(str(num))

        res=[]
        if num<0:                    
            s=sorted(s[1:], reverse=True)
            return int("".join(s))*-1
        elif num>0:
            minn='9'
            for n in range(len(s)):
                if s[n]!='0' and s[n]<minn:
                    minn=s[n]
                    s[0],s[n]=s[n],s[0]                    
            s=sorted(s[1:])
            print(s)
            return int("".join([minn]+s))
        else:
            return 0


    