# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor=0
        for num in nums:
            xor^=num
        
        n=2**maximumBit-1
        res=[]
        for j in range(len(nums)):
            res.append(n-xor)
            xor^=nums.pop()
        
        return res