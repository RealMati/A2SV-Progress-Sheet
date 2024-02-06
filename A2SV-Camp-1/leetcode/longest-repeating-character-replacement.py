class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        maxAns=0
        l=0

        for r in range(len(s)):
            count[s[r]]+=1

            if (r-l+1)-max(count[key] for key in count)>k:
                maxAns=max(maxAns,(r-l))
                while (r-l+1)-max(count[key] for key in count)>k:
                    if count[s[l]]>1: count[s[l]]-=1
                    else: del count[s[l]]
                    l+=1

        maxAns=max(maxAns,(len(s)-l))
        return maxAns
        
                
