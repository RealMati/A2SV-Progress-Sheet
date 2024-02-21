# sys.setrecursionlimit(1<<30)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        def c(x,n):
            if n==0: return 1
            if n==1: return x
            if n%2:
                return (x*c((x%(10**9 +7)),n-1))%(10**9 +7)
            else:
                return (c(((x**2)%(10**9 +7)),n//2))%(10**9 +7)

        one=(c(5,(n+1)//2))%(10**9 +7)
        two=(c(4,n//2))%(10**9 +7)
        # print(one,two)
        return (one*two)%(10**9 +7) 
