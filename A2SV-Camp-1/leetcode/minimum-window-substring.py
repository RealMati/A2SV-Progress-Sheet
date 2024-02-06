class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCt=Counter(t)
        window=defaultdict(int)
        l=0
        minWindow=s+s

        if len(s)<len(t):
            return ""

        for r in range(len(s)):
            if s[r] in tCt:
                window[s[r]]+=1

            if all(tCt[key]<=window[key] for key in tCt):
                while all(tCt[key]<=window[key] for key in tCt) and l<=r:
                    if s[l] in window: window[s[l]]-=1
                    l+=1

                if len(minWindow)>r-l+1:
                    minWindow=s[l-1:r+1]

        if minWindow==s+s:
            return ""
        return minWindow
                