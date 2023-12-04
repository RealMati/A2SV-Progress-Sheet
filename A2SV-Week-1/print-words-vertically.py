class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        maxx=0
        for i in s:
            maxx=max(maxx,len(i))
        res=[]
        for idx in range(maxx):
            ans=''  
            last=maxx
            for word in range(len(s)):
                if idx>=len(s[word]):
                    ans+=' '
                else:
                    ans+=s[word][idx]
                    last=word
            res.append(ans.rstrip())
        return res
        


        