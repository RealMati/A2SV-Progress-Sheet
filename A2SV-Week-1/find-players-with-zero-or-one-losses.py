class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            
        losers=set()
        winners=set()
        multipleloser=set()

        for win,lose in matches:
            if lose in losers:
                multipleloser.add(lose)
            else:
                losers.add(lose)
            winners.add(win)
        
        return [sorted(winners-losers),sorted(losers-multipleloser)]
            