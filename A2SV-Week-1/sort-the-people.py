class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        #INSERTION SORT
        result=[0]*(max(heights)+1)
        for i in range(len(heights)):
            result[heights[i]]=names[i]
        res=[]
        for i in range(len(result)-1,-1,-1):
            if result[i]:
                res+=[result[i]]
        return res
        
        