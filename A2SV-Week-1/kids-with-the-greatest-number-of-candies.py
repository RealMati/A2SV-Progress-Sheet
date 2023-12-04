class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        for candy in range(len(candies)):
            if candies[candy]+extraCandies>=maxx:
                candies[candy]=True
            else:
                candies[candy]=False
        return candies
            
        