class Solution:
    def balancedString(self, s: str) -> int:
        minCt=float('inf')
        freq=Counter(s)
        l=0
        if max(freq.values()) <= len(s)//4:
            return 0
            
        for r in range(len(s)):
            freq[s[r]]-=1

            if max(freq.values()) <= len(s)//4:
                while max(freq.values())<= len(s)//4 and l<=r:
                    freq[s[l]]+=1
                    l+=1

                minCt=min(minCt,r-l+2)
                
        return minCt
                
                
