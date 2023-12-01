class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=j=0
        res=''
        while i<len(word1) and j<len(word2):
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        if i<len(word1):
            res+=word1[i:]
        elif j<len(word2):
            res+=word2[j:]
        return res
        