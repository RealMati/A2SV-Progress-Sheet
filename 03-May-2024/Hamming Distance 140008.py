# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        i=0
        res=0
        while i<max(int.bit_length(x), int.bit_length(y)):
            if x&1<<i!=y&1<<i:
                res+=1
                # print(i, res)
            i+=1
            # print(i)
        return res
                