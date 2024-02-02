class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l=0
        res=[]

        for r in range(len(words)):
            if sorted(words[l])!=sorted(words[r]):
                res.append(words[l])
                l=r

        res.append(words[l])
        return res