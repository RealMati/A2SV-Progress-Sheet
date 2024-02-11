class Solution:
    def numberOfWays(self, s: str) -> int:
        zeroprefix=oneprefix=res=0
        zerosuffix=s.count("0")
        onesuffix=len(s)-zerosuffix

        for num in s:
            if num=="0":
                res+=onesuffix*oneprefix
                zeroprefix+=1
                zerosuffix-=1
            else:
                res+=zerosuffix*zeroprefix
                oneprefix+=1
                onesuffix-=1

        return res
         