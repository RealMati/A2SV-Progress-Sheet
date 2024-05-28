# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Trie:
    def __init__(self):
        self.children = [None, None]
        self.end = False

class Solution:
    def __init__(self):
        self.root = Trie()

    def findMaximumXOR(self, nums: List[int]) -> int:
        maxDig=0
        for num in nums:
            maxDig=max(maxDig, int.bit_length(num))
        
        for num in nums:
            cur=self.root
            for i in range(maxDig-1, -1, -1):
                if num&1<<i!=0:
                    if cur.children[1]==None:
                        cur.children[1]=Trie()
                    cur=cur.children[1]
                else:
                    if cur.children[0]==None:
                        cur.children[0]=Trie()
                    cur=cur.children[0]
            cur.end = True
        
        cur=self.root
        def maxForNum(num):
            cur=self.root
            xor=0
            for i in range(maxDig-1, -1, -1):
                if num&1<<i!=0:
                    if cur.children[0]:
                        xor+=2**i
                        cur=cur.children[0]
                    else:
                        cur=cur.children[1]
                else:
                    if cur.children[1]:
                        xor+=2**i
                        cur=cur.children[1]
                    else:
                        cur=cur.children[0]
            return xor

        maxx=0
        for num in nums:
            maxx=max(maxx, maxForNum(num))
        return maxx
            