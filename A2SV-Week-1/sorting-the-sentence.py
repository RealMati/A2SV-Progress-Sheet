class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        

        s=s.split()

        res=[0]*len(s)

        for word in s:
            res[int(word[-1])-1]=word[:-1]

        return " ".join(res)