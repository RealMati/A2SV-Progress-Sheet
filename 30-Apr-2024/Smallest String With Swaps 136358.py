# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent={i:i for i in range(len(s))}
        rank={i:0 for i in range(len(s))}  
        carry={i:[s[i],i] for i in range(len(s))}  


        def find(x):
            cur = x
            while cur != parent[cur]:
                cur = parent[cur]

            cur1=x
            while cur1!=parent[cur1]:
                parent[cur1]=cur
                cur1=parent[cur1]
            
            return cur

        def union(a, b):
            parentA = find(a)
            parentB = find(b)
            rankA=rank[parentA]
            rankB=rank[parentB]

            if parentA!=parentB:
                if rankA>rankB:
                    parent[parentB] = parentA
                    carry[parentA].extend(carry[parentB])
                elif rankA<rankB:
                    parent[parentA] = parentB
                    carry[parentB].extend(carry[parentA])
                else:
                    parent[parentA] = parentB
                    carry[parentB].extend(carry[parentA])
                    rank[parentB]+=1

        for x,y in pairs:
            union(x,y)
        # print(parent)
        sett=set()
        for i in range(len(s)):
            sett.add(find(i))

        def custom_sort(x):
            if isinstance(x, int):
                return 0, x  
            else:
                return 1, str(x)

        res=[""]*len(s)
        for par in sett:
            carry[par]=sorted(carry[par], key=custom_sort)
            ind=len(carry[par])//2
            for i in range(len(carry[par])//2):
                res[carry[par][i]]= carry[par][ind]
                ind+=1
        # print(sett)
        # print(carry)
        return "".join(res)
            
                


