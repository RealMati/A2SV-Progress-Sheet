class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize=len(s1)
        if windowSize>len(s2):
            return False
        
        freq=Counter(s2[:windowSize])
        check=Counter(s1)

        if freq==check:
            return True
        
        for i in range(windowSize,len(s2)):
            if freq[s2[i-windowSize]]>1: freq[s2[i-windowSize]]-=1
            else: del freq[s2[i-windowSize]]
            
            freq[s2[i]]+=1

            if freq==check:
                return True
        
        return False
        