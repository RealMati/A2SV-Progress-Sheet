class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        summ=0
        while True:
            summ+=(n%10)**2
            n=n//10
            if n==0:
                if summ==1:
                    return True
                elif summ<10:
                    if summ==7: return True
                    return False
                n=summ
                summ=0
                
        return summ
