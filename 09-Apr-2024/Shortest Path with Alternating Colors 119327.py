# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        res = [-1] * n

        graph = defaultdict(list)

        for u, v in redEdges:
            graph[u].append((v, "r"))

        for u, v in blueEdges:
            graph[u].append((v, "b"))

        visited = defaultdict(int)
        q = deque()
        q.append((0, "f"))
        moves = -1

        while q:
            moves += 1
            for i in range(len(q)):
                cur, now = q.popleft()
                if res[cur]==-1:
                    res[cur] = moves

                for nbs, next in graph[cur]:
                    if visited[(cur,nbs)] < 2 and next != now:
                        q.append((nbs, next))
                        visited[(cur,nbs)]+=1

        return res
