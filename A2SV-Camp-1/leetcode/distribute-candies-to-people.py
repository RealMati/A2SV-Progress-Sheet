class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res=[0]*num_people
        idx=0
        val=0

        while candies>0:
            val+=1
            res[idx]+= val if val<candies else candies
            candies -= val if val<candies else candies

            idx = (idx+1) % num_people

        return res
