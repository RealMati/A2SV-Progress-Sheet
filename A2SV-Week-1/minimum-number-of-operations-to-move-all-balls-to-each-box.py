class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        positions=[]
        res=[]

        for idx,letter in enumerate(boxes):
            if letter=="1": positions.append(idx)
        
        for idx,letter in enumerate(boxes):
            moves=0
            for pos in positions:
                moves+=abs(pos-idx)
            res.append(moves)

        return res