# Problem: Largest Odd Number in String - https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
            


        for right in range(len(num)-1,-1,-1):
            if int(num[right])%2:
                return num[:right+1]
        return ""