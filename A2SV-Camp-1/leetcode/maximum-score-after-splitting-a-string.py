class Solution:
    def maxScore(self, s: str) -> int:
        ones=s.count('1')
        zeros=0
        maxx=0

        for n in range(len(s)):
            if s[n]=='1':
                ones-=1
            elif n!=len(s)-1:
                zeros+=1
            
            maxx=max(maxx,zeros+ones)
        
        return maxx
        


               