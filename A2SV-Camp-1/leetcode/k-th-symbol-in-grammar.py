class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def c(n,k):
            if n<=0:
                return
            if n==1:
                if k==1:
                    return 0
            p = c(n-1,(k-1)//2+1)
            if p==0:
                if k%2==0:
                    return 1
                else:
                    return 0
            else:
                if k%2==0:
                    return 0
                else:
                    return 1
        return c(n,k)