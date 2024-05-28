# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1
        if x==1: return 1
        if x==-1 and n%2: return -1
        if x==-1 and n%2==0: return 1

        if n<0: num=0
        else: num=1
        n=abs(n)
        def c(x,n):
            if n==1: return x
            if n%2:
                return x*c(x,n-1)
            else:
                return c(x**2,n//2)
            
        return c(x,n) if num else c(1/x,n)
