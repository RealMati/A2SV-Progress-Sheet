# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lads=[]

        for i in range(len(heights)-1):
            if heights[i]<heights[i+1]:
                minus=heights[i+1]-heights[i]

                if ladders:
                    heappush(lads, minus)
                    ladders-=1
                elif lads and lads[0]<=bricks and minus>lads[0]:
                    bricks-=lads[0]
                    heapreplace(lads, minus)
                elif minus<=bricks:
                    bricks-=minus
                else:
                    return i
            # print(lads, bricks, i)

        return len(heights)-1
        