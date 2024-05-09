# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def tri(n):
            if n<2: return n
            if n==2: return 1

            return tri(n-3)+tri(n-2)+tri(n-1)
            
        return tri(n)