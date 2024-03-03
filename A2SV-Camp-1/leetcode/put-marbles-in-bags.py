class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairSum = []
        for i in range(1, len(weights)):
            pairSum.append(weights[i] + weights[i-1])

        pairSum.sort()
        maxx = 0
        minn = 0

        for i in range(k-1):
            minn += pairSum[i]
            maxx += pairSum[len(pairSum)-1-i]
            
        return maxx - minn
        