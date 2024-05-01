# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=na=0
        b=nb=0

        def handle(num, a, b):
            idx=int.bit_length(num)
            for i in range(idx):
                if num & 1<<i != 0:
                    if a&1<<i==0 and b&1<<i==0:
                        b |= 1<<i
                    elif a&1<<i==0 and b&1<<i!=0:
                        b ^= 1<<i
                        a |= 1<<i
                    elif a&1<<i!=0 and b&1<<i==0:
                        a ^= 1<<i
            return a, b
                
        for num in nums:
            if num>=0:
                a,b=handle(num, a, b)
            else:
                na,nb=handle(-num, na, nb)

        print(bin(a))
        print(bin(b))
        print(bin(na))
        print(bin(nb))
        print(int.bit_length(-2))
        return a^b if a!=0 or b!=0 else (na^nb)*-1
                    
