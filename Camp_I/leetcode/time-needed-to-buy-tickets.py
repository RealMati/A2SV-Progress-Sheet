class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while tickets[k]!=0:
            for i in range(len(tickets)):
                if tickets[i]==0:
                    continue
                else:
                    tickets[i]-=1
                    count+=1
                    if i == k and tickets[i]==0:
                        break
        return count