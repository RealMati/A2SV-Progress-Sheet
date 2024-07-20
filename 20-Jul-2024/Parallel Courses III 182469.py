# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        incoming = [0] * (n + 1)

        for prev, next in relations:
            graph[next].append(prev)
            incoming[prev] += 1

        q=deque()
        memo=defaultdict(int)

        for node in range(1, n+1):
            if incoming[node]==0:
                q.append(node)
                memo[node]=time[node-1]
        
        while q:
            for i in range(len(q)):
                node=q.popleft()
                for nbs in graph[node]:
                    memo[nbs]=max(memo[nbs], time[nbs-1] + memo[node])
                    incoming[nbs]-=1
                    if incoming[nbs]==0:
                        q.append(nbs)
        
        # print(memo)
        return max(memo.values())

