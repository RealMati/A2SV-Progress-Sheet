class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        res=''
        min=strs[0]
        for i in strs:
            if len(i)<len(min):
                min=i
        for n in range(len(min)):
            if strs[0][n]!=strs[-1][n]:
                return res
            res+=strs[-1][n]
        return res                
