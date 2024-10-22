class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
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
                    if d<dist[nbs] and d<disappear[nbs]:
                        dist[nbs]=d
                        heappush(heap, (d, nbs))

           
            return dist
        
        fromSrc = dijkstra(0)
        fromSrc = [val if val!=float('inf') else -1 for val in fromSrc]

        return fromSrc





