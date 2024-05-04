# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ct=0

        from math import gcd
            
        for l in range(len(nums)):
            if nums[l]==k: ct+=1
            res=nums[l]
            if res<k: continue
            
            for r in range(l+1, len(nums)):
                res=gcd(nums[r],res)
                if res==k: ct+=1
                if res<k:
                    break
                
        return ct
