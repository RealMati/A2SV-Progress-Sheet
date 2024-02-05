class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first=0
        second=0
        res=[]

        while first<len(firstList) and second<len(secondList):
            if firstList[first][0]<=secondList[second][1] and secondList[second][0]<=firstList[first][1]:
                res.append([max(firstList[first][0], secondList[second][0]), min(firstList[first][1], secondList[second][1])])
                
                if firstList[first][1]>secondList[second][1]:
                    second+=1
                else:
                    first+=1

            elif firstList[first][0]>secondList[second][1]:
                second+=1
            elif secondList[second][0]>firstList[first][1]:
                first+=1
        
        return res


        

