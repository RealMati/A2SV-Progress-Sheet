# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited=set()
        def dfs(cur, pos, dic):
            if cur in dic:
                return pos-dic[cur]
            if cur in visited:
                return None
            
            if edges[cur]==-1: return None
            dic[cur]=pos
            visited.add(cur)
            return dfs(edges[cur], pos+1, dic)
        
        res=-1
        for i in range(len(edges)):
            if i not in visited and edges[i]!=-1:
                ans=dfs(i, 0, {})
                if ans:
                    res=max(ans,res)
            visited.add(i)

        return res