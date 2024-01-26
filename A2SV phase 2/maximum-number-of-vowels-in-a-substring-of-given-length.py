class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels={'a', 'e', 'i', 'o', 'u'}
        maxCount=0

        for idx in range(k):
            if s[idx] in vowels:
                maxCount+=1
            
        curCount=maxCount

        for r in range(k, len(s)):
            if s[r-k] in vowels:
                curCount-=1
            if s[r] in vowels:
                curCount+=1
            
            maxCount=max(maxCount, curCount)

        return maxCount

