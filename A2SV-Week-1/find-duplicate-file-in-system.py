class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        from collections import defaultdict
        contentdic=defaultdict(list)

        for path in paths:

            splpath=path.split()

            for i in splpath[1:]:
                cont=i.split(".txt")
                contentdic[cont[1]].append(splpath[0]+"/"+cont[0]+".txt")
        
        res=[]

        for i in contentdic.values():

            if len(i)>1:
                res.append(i)

        return res
                