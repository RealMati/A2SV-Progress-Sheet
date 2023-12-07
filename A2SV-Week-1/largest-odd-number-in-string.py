class Solution:
    def largestOddNumber(self, num: str) -> str:
            
        right=len(num)-1

        while right>=0:
            if int(num[right])%2:
                return num[:right+1]
            right-=1

        return ""