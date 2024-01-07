class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        p1=p2=0

        if len(name)>len(typed):
            return False

        while p1<len(name) and p2<len(typed):
            if name[p1]!=typed[p2]:
                return False
            if p2+1<len(typed) and p1+1<len(name) and name[p1+1]==typed[p2+1]:
                p2+=1
                p1+=1
            elif p2+1<len(typed) and name[p1]==typed[p2+1]:
                p2+=1
            else:
                p1+=1
                p2+=1

        if p2==len(typed) and p1==len(name): return True
        else: return False
        