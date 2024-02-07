class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix=[0]*len(s)

        for start,end,val in shifts:
            if val:
                prefix[start]+=1
                if end+1<len(s): prefix[end+1]-=1
            else:
                prefix[start]-=1
                if end+1<len(s): prefix[end+1]+=1
        
        res=[]
        for i in range(len(s)):
            if i-1>=0: prefix[i]+=prefix[i-1]
            res.append(chr(((ord(s[i])+prefix[i])-97)%26 + 97))

        return "".join(res)