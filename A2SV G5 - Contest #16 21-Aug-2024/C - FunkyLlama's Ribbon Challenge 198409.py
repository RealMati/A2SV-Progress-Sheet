# Problem: C - FunkyLlama's Ribbon Challenge - https://codeforces.com/gym/523525/problem/C

""" 
memo = {}

n, a, b, c = list(map(int, input().split()))


def dp(num):
    if num in memo:
        return memo[num]

    if num < 0:
        return float('-inf')

    if num == 0:
        return 0

    maxx = float('-inf')
    for opt in [a, b, c]:
        maxx = max(maxx, 1 + dp(num-opt))

    memo[num] = maxx
    return maxx


res = dp(n)
print(res if res != float('-inf') else 0)
 """

memo = {0: 0}

n, a, b, c = list(map(int, input().split()))

for i in range(1, n+1):
    maxx = float('-inf')
    for opt in [a, b, c]:
        if i >= opt:
            maxx = max(maxx, 1 + memo[i-opt])
    # print(i, maxx)
    memo[i] = maxx

print(memo[n] if memo[n] != float('-inf') else 0)
