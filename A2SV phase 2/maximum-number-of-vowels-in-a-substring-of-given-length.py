class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a', 'e', 'i', 'o', 'u'}

        maxx=0
        for i in range(k):
            if s[i] in vowels:
                maxx+=1
        cur=maxx
        for idx in range(k,len(s)):
            if s[idx-k] in vowels:
                cur-=1
            if s[idx] in vowels:
                cur+=1
            maxx=max(maxx,cur)
        
        return maxx