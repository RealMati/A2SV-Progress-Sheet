class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        pg=ps=ct=0
        g.sort()
        s.sort()

        while pg<len(g) and ps<len(s):
            if g[pg]>s[ps]:
                ps+=1
            else:
                ct+=1
                ps+=1
                pg+=1
        return ct