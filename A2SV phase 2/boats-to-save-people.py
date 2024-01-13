class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        ct=0

        while l<r:
            summ=people[l]+people[r]
            if summ>limit:
                ct+=1
                r-=1
            else:
                ct+=1
                r-=1
                l+=1
        if l==r:
            ct+=1
        return ct

        