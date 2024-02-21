class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        left = bin(left)[2:]
        right = bin(right)[2:]
        n = len(left)
        if n!=len(right):
            return 0
        else:
            for i in range(n):    
                if left[i] == "1" and right[i] == "1":
                    ans+=pow(2,n-i-1)
                elif left[i]=="1" and right[i]=="0" or left[i]=="0" and right[i]=="1":
                    break
        return ans
                