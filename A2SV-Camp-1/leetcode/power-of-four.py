class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def c(n):
            if n==1: return True
            if n<1: return False

            return c(n/4)
        return c(n)