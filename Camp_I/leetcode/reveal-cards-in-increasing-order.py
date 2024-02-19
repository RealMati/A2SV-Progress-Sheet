class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:  
        '''
        res = [0]*len(deck)
        deck.sort()
        queue = [i for i in range(len(deck))]
        while deck:
            for i in range(len(queue)):              #great efficiency
                res[queue[i]] = deck.pop(0)
                if i+1<len(queue):
                    queue.append(queue.pop(i+1))
                else:
                    continue
        return res
        '''
        '''
        deck.sort(reverse = True)
        queue = [deck[0]]
        for i in range(1,len(deck)):
            queue = [queue.pop()]+queue     #slow efficiency 
            queue = [deck[i]] + queue
        return queue
        '''
        deck.sort(reverse = True)
        queue = deque()
        for num in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(num)
        return queue