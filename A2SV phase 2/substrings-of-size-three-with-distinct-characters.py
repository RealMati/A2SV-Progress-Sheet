class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        freq=Counter(s[:3])
        res=0

        if len(freq)==3:
                res+=1
        for i in range(3,len(s)):
            if freq[s[i-3]]>1: freq[s[i-3]]-=1
            else: del freq[s[i-3]]

            freq[s[i]]+=1

            if len(freq)==3:
                res+=1

        return res