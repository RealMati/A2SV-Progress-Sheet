class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        if x<0:
            return False
        while len(s)>=2:
            if s[0]==s[-1]:
                s=s[1:-1]
            else:
                return False
        return True
        
