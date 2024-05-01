# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        res=0

        for i in range(int.bit_length(num)):
            if num&1<<i==0:
                res|=1<<i

        return res
