# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent={i:i for i in range(len(strs))}
        rank={i:0 for i in range(len(strs))}

        def union(a,b):
            parentA=find(a)
            parentB=find(b)

            rankA=rank[a]
            rankB=rank[b]

            if parentA!=parentB:
                if rankA>rankB:
                    parent[parentB]=parentA
                    rankA+=rankB
                else:
                    parent[parentA]=parentB
                    rankB+=rankA

        def find(x):
            cur=x
            while parent[cur]!=cur:
                cur=parent[cur]
            
            cur2=x
            while cur2!=cur:
                next=parent[cur2]
                parent[cur2]=cur
                cur2=next   

            return cur



        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                notSame=0
                for ptr in range(len(strs[i])):
                    if strs[i][ptr]!=strs[j][ptr]:
                        notSame+=1
                        if notSame>2:
                            break
                if notSame<=2:
                    union(i,j)
        
        sett=set()

        for idx in range(len(strs)):
            sett.add(find(idx))

        return len(sett)
