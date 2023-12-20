class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res=[]
        strings=[]
        strings.extend(s)

        for i in range(0,len(s),2*k):
            res.append(strings[i:i+k][::-1])
            res.append(strings[i+k:i+2*k])

        for i in range(len(res)):
            res[i]="".join(res[i])
        return "".join(res)

        