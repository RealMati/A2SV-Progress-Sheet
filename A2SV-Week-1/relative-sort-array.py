class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count=[0]*(max(arr1)+1)
        extra=[]
        for i in arr1:
            count[i]+=1
            if i not in arr2:
                extra+=[i]
        extra.sort()
        res=[]
        for i in arr2:
            res+=[i]*count[i]
        res+=extra
        return res
        