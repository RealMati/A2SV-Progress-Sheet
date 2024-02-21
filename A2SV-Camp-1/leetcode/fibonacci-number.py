class Solution:
    def fib(self, n: int) -> int:
        @lru_cache        
        def c(n):
            if n==0: return 0
            if n==1: return 1

            return c(n-1)+c(n-2)
        return c(n)