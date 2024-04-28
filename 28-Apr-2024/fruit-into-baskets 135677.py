# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        maxx=0
        dic=defaultdict(int)

        for r in range(len(fruits)):
            dic[fruits[r]]+=1
            if len(dic)>2:
                maxx=max(maxx,r-l)
                while len(dic)>2:
                    if dic[fruits[l]]>1: dic[fruits[l]]-=1
                    else: del dic[fruits[l]]
                    l+=1
        
        maxx=max(maxx,len(fruits)-l)
        return maxx

