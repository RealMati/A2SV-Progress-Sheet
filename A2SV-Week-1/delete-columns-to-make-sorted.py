class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ct=0
        for ind in range(len(strs[0])):
            for w in range(len(strs)-1):
                if strs[w][ind]<=strs[w+1][ind]:
                    res=False
                else:
                    res=True
                    break
            if res:
                ct+=1
        return ct

        