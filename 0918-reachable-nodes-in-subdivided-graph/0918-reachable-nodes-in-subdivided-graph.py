class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph=defaultdict(list)
       
        for a,b,w in edges:
            graph[a].append((b,w))
            graph[b].append((a,w))
          
        heap=[(0,0)]
        dist = [float('inf') for _ in range(n)]
        dist[0]=0
        processed=set()

        #figures out in how many min move we can reach the nodes but not the inbetween nodes
        while heap:
            cost, cur = heappop(heap)
            if cur in processed: continue
            processed.add(cur)

            for nbs, w in graph[cur]:
                d = cost+w+1
                if d<=maxMoves and d<dist[nbs]:
                    dist[nbs]=d
                    heappush(heap, (d, nbs))

        ans = 0

        for a in dist:
            #if we can reach this original node count it
            if a!=float('inf'):
                ans+=1

        #figures out the inbetween nodes
        for a,b,w in edges:
            x,y=0,0

            #if one of the nodes isnt reachable then we wont also reach the inbetweens
            if dist[a]!=float('inf'):
                x=maxMoves-dist[a]
            if dist[b]!=float('inf'):
                y=maxMoves-dist[b]

            #if we counted the inbetween nodes in overlapping manner take the whole inbetween nodes
            ans += min(w, x+y)

        return ans




        




