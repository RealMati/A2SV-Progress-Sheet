# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D


n = int(input())
parent = [i for i in range(n + 1)]
rank = [1 for i in range(n + 1)]
order = [[i] for i in range(n + 1)]


def find(x):
    cur = x
    while cur != parent[cur]:
        cur = parent[cur]

    cur1 = x
    while cur1 != parent[cur1]:
        parent[cur1] = cur
        cur1 = parent[cur1]

    return cur


def union(a, b):
    parentA, parentB = find(a), find(b)
    rankA, rankB = rank[parentA], rank[parentB]

    if parentA != parentB:
        if rankA > rankB:
            parent[parentB] = parentA
            rank[parentA] += rank[parentB]
            order[parentA].extend(order[parentB])
        else:
            parent[parentA] = parentB
            rank[parentB] += rank[parentA]
            order[parentB].extend(order[parentA])


for i in range(n-1):
    n, k = list(map(int, input().split()))
    union(n, k)

print(*order[find(1)])
