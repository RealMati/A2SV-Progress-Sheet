# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        dic=set()
        maxx=0

        for r in range(len(s)):
            if s[r] not in dic:
                dic.add(s[r])
            else:
                maxx=max(maxx,r-l)
                while s[r]!=s[l]:
                    dic.remove(s[l])
                    l+=1

                l+=1
        if len(s)>0: maxx=max(maxx,r-l+1)
        return maxx