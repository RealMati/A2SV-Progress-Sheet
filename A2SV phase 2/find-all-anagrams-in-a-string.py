class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize=len(p)

        check=Counter(p)
        freq=Counter(s[:windowSize])
        res=[]
        if freq==check:
            res.append(0)
        
        for i in range(windowSize,len(s)):
            if freq[s[i-windowSize]]>1: freq[s[i-windowSize]]-=1
            else: del freq[s[i-windowSize]]

            freq[s[i]]+=1
    
            if freq==check:
                res.append(i-windowSize+1)
        
        return res

