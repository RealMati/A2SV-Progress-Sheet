# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {i: i for i in s1+s2}
        rank = {i: 0 for i in s1+s2}
        smallest = {i: i for i in s1+s2}

        def union(a, b):
            parentA = find(a)
            parentB = find(b)
            rankA=rank[parentA]
            rankB=rank[parentB]

            if parentA!=parentB:
                if rankA>rankB:
                    parent[parentB] = parentA
                    smallest[parentA]=min(smallest[parentA],smallest[parentB])
                elif rankA<rankB:
                    parent[parentA] = parentB
                    smallest[parentB]=min(smallest[parentA],smallest[parentB])
                else:
                    parent[parentA] = parentB
                    smallest[parentB]=min(smallest[parentA],smallest[parentB])
                    rank[parentB]+=1

        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]

            cur1 = x
            while cur1 != parent[cur1]:
                cur1=parent[cur1]

            return cur

        for i in range(min(len(s1), len(s2))):
            union(s1[i], s2[i])

        res=[]
        for i in baseStr:
            res.append(smallest[find(i)] if i in parent else i)
            
        # print(parent)
        # print(smallest)
        return "".join(res)
