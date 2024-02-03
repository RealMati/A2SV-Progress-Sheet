class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minop=0
        for i in range(k):
            if blocks[i]=="W":
                minop+=1
        
        curop=minop
        for i in range(k,len(blocks)):
            if blocks[i-k]=="W":
                curop-=1
            if blocks[i]=="W":
                curop+=1
            
            minop=min(minop,curop)
        
        return minop