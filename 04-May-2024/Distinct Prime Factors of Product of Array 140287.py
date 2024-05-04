# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        sett=set()
        for m in nums:
            d=2
            while m>=d*d:
                if m%d==0:
                    sett.add(d)
                while m%d==0:
                    m//=d
                d+=1
            if m!=1: sett.add(m)
        # print(sett)
        return len(sett)