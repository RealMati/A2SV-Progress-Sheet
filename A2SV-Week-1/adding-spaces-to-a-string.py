class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        sp=0
        for i in spaces:
            s=s[:i+sp]+" "+s[i+sp:]
            sp+=1
        return s