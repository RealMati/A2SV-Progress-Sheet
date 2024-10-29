class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res=[]

        for idx in range(len(height)-1):
            if height[idx]>threshold:
                res.append(idx+1)
        
        return res