# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0

        for i in range(32):
            ct=0
            for num in nums:
                ct+= 1 if num & 1<<i else 0
            res += 1 if (k&1<<i==0 and ct%2) or (k&1<<i and ct%2==0)  else 0

        return res
