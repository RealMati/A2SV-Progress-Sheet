# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for i in range(len(strs)):
            strs[i]=[sorted(strs[i]), strs[i]]
        
        strs.sort()

        res=[]
        check=strs[0][0]
        ans=[]
        for sortedd, normal in strs:
            if sortedd==check:
                ans.append(normal)
            else:
                res.append(ans)
                ans=[normal]
                check=sortedd
        if ans: res.append(ans)
        return res