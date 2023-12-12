class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=s.split()

    
        return " ".join(res[::-1])
        