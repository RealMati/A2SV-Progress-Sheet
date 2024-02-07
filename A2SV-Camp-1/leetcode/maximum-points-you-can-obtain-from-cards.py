class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxSum=0
        window=len(cardPoints)-k
        summ=sum(cardPoints)
  
        for i in range(window):
            maxSum+=cardPoints[i]
            
        curSum=maxSum
        maxSum=summ-curSum

        for i in range(window,len(cardPoints)):
            curSum-=cardPoints[i-window]
            curSum+=cardPoints[i]
            maxSum=max(maxSum,summ-curSum)

        return maxSum