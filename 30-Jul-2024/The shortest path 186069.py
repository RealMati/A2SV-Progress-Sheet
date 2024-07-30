# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import deque, defaultdict

n, m = map(int, input().split())

a, b = map(int, input().split())

graph = defaultdict(set)
for _ in range(m):
    line = list(map(int, input().split()))
    graph[line[0]].add(line[1])
    graph[line[1]].add(line[0])

queue = deque([a])
visited = set()
l = 0
parents = {}

while queue:
    node = queue.popleft()
    visited.add(node)

    if node == b:
        break

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
            parents[neighbour] = node

if b in visited:
    path = [b]
    while path[-1] != a:
        path.append(parents[path[-1]])

    print(len(path) - 1)
    print(*(reversed(path)))
else:    
    print(-1)