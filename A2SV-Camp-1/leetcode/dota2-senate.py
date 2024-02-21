class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        c=Counter(senate)
        removedR=removedD=0
        r=c['R']
        d=c['D']
        q=deque(senate)

        while r and d:
            if q[0]=='D' and removedD==0:
                r-=1
                removedR+=1
                q.append('D')
            elif q[0]=='D' and removedD!=0:
                removedD-=1
            elif q[0]=='R' and removedR!=0:
                removedR-=1
            else:
                d-=1
                removedD+=1
                q.append('R')
            q.popleft()

        return "Dire" if d else"Radiant"
        


