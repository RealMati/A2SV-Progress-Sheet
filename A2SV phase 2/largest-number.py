class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=[]
        for n in nums:
            s.append(str(n))
        res=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]+s[j] < s[j]+s[i]:
                    s[i],s[j]=s[j],s[i]
        
        return str(int("".join(s)))
                