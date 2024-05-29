# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def findClosest(house):
            if (house <= heaters[0]):
                return heaters[0]-house

            if (house >= heaters[(len(heaters))- 1]):
                return house-heaters[len(heaters) - 1]

            l=0
            r=len(heaters)-1
            immediateLess=immediateGreater=None
            
            while l<=r:
                mid = (l + r) // 2
                if heaters[mid]==house:
                    return 0
                if heaters[mid]<house:
                    immediateLess=heaters[mid]
                    l=mid + 1
                else:
                    immediateGreater=heaters[mid]
                    r=mid - 1  
            
            if  immediateGreater and immediateLess:
                ans=min(immediateGreater-house, house-immediateLess)
            elif immediateGreater:
                ans=immediateGreater-house
            else:
                ans=house-immediateLess
            # print(house, ans, immediateGreater, immediateLess)
            return ans

        res=0
        for house in houses:
            res=max(res, findClosest(house))
        return res
