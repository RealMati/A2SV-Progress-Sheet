# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        sameFrontandBack=set()

        min_num=float('inf')

        for idx,num in enumerate(fronts):


                if backs[idx]==num:
                    sameFrontandBack.add(num)
        
        for idx,num in enumerate(fronts):
            if num not in sameFrontandBack:
                min_num=min(min_num,num)
        for idx,num in enumerate(backs):
            if num not in sameFrontandBack:
                min_num=min(min_num,num)

        if min_num==float('inf'):
            return 0
        else:
            return min_num 

        