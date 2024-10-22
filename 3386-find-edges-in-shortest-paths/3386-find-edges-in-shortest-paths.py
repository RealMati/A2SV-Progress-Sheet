class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        for a,b,w in edges:
            graph[a].append((b,w))
            graph[b].append((a,w))

        def dijkstra(src):
            heap=[(0,src)]
            dist = [math.inf for _ in range(n)]
            processed=set()
            dist[src]=0

            while heap:
                cost, cur = heappop(heap)
               
                if cur in processed: continue
                processed.add(cur)

                for nbs, w in graph[cur]:
                    d=cost+w
                    if d<dist[nbs]:
                        dist[nbs]=d
                        heappush(heap, (d, nbs))

           
            return dist
        
        fromSrc = dijkstra(0)
        fromDest = dijkstra(n-1)
        trueVal = fromSrc[-1]
        # print(fromSrc, fromDest)
        
        res=[]
       
        for a,b,w in edges:
            if trueVal!=float('inf') and (fromSrc[a]+w+fromDest[b]==trueVal or fromSrc[b]+w+fromDest[a]==trueVal): 
                res.append(True)
            else:
                res.append(False)
        
        return res





