# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        m=n
        while m:
            original=m
            primes=[]
            d=2
            while m>=d*d:
                while m%d==0:
                    primes.append(d)
                    m//=d
                d+=1
            
            if m!=1: 
                primes.append(m)
            
            summ=sum(primes)
            # print(primes,m)
            if original==summ: return original
            m=summ
          

        
        