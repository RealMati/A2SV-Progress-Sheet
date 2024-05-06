# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xffffffff

        while b!=0:
            temp=a
            a = (a ^ b)&mask
            b = ((temp&b)<<1)&mask
        
        if a > mask//2:
            return ~(a^mask)
        else : 
            return a