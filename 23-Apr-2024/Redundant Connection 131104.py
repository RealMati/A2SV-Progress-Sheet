# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph={}
        rank=defaultdict(int)
        parent={i:i for i in range(1,len(edges)+1)}

        for i,j in edges:
            grpA=parent[i]
            grpB=parent[j]
            
            if grpA==grpB:
                res=[i,j]
            for city in parent:
                if parent[city]==grpB:
                    parent[city]=grpA        

        # print(parent)
        return res