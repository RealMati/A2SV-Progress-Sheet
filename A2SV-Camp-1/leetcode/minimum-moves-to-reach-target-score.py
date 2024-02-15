class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op=0

        while maxDoubles and target!=1:
            op+=(target%2)
            target=target//2
            maxDoubles-=1
            op+=1
        
        op+=(target-1)
        return op