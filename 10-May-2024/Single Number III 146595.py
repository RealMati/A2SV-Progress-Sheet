# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mash = nmash = 0

        for num in nums:
            if num >= 0:
                mash ^= num
            else:
                nmash ^= num

        def do(mash, pos):
            for i in range(int.bit_length(mash)):
                if mash&1<<i!=0:
                    global a,b
                    a=b=0
                    for num in nums:
                        if pos!=(num>=0):
                            continue

                        if num&1<<i and i<int.bit_length(num):
                            a^=num
                        if num&1<<i==0 and i<int.bit_length(num):
                            b^=num
                    break
                    
        if mash and not nmash: do(mash, True)
        elif nmash and not mash: do(nmash, False)
        else: return [mash,nmash]


        return [a,b]