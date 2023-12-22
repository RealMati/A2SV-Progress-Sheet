class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(len(s)//2):
            temp=s[i]
            s[i]=s[n-1-i]
            s[n-1-i]=temp
        return s

        