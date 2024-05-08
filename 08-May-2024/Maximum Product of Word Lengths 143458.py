# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        custom_bit = [["0"]*26 for i in range(len(words))]

        for i in range(len(words)):
            for ch in words[i]:
                custom_bit[i][ord(ch)-97]="1"

            custom_bit[i]=int("".join(custom_bit[i]), 2)

        maxx=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if custom_bit[i]&custom_bit[j]==0:
                    maxx=max(maxx, len(words[i]*len(words[j])))
                    
        return maxx


        return 0
        
        
        
            
