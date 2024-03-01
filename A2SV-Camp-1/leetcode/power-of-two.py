class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        def c(num):
            if num%2==0:
                if num==0: return False
                if num==1: return True

                return c(num//2)
            return num
        return c(n)==1
