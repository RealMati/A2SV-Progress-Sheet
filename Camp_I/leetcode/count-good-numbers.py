class Solution:
    def countGoodNumbers(self, n: int) -> int:
        res = 1
        pow(4,n//2,10**9+7)
        if n%2==0:
            res*= pow(4,n//2,10**9+7)
            res*= pow(5,n//2,10**9+7)
        else:
            res*= pow(4,n//2,10**9+7)
            res*= pow(5,(n//2)+1,10**9+7)
        return res%(10**9+7)