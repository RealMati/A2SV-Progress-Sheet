class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        res=[]

        for str in strs:
            key="".join(sorted(str))

            if key not in dic:
                dic[key]=[str]
            else:
                dic[key].append(str)
        
        for value in dic.values():
            res.append(value)

        return res
        