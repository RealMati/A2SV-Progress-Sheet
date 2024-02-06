class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count=defaultdict(int)
        minn=len(cards)+1
        l=0

        for r in range(len(cards)):
            count[cards[r]]+=1

            if count[cards[r]]==2:
                while count[cards[r]]==2:
                    if count[cards[l]]>1: count[cards[l]]-=1
                    else: del count[cards[l]]
                    l+=1
                minn=min(minn,r-l+2)

        if minn==len(cards)+1: return -1
        return minn
        
                
