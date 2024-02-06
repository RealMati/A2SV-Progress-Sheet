class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count={"T":0,"F":0}
        maxAns=0
        l=0

        for r in range(len(answerKey)):
            count[answerKey[r]]+=1

            if min(count["T"],count["F"])>k:
                maxAns=max(maxAns,(r-l))
                while min(count["T"],count["F"])>k:
                    count[answerKey[l]]-=1
                    l+=1

        maxAns=max(maxAns,(len(answerKey)-l))
        return maxAns
        
                
