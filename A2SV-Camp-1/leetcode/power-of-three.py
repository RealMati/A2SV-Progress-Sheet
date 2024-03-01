class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0: return False
        def c(num):
            if num%3==0:
                if num==0: return False
                if num==1: return True

                return c(num//3)
            return num
        return c(n)==1
