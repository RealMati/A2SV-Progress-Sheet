# Problem: B - Instructions - https://codeforces.com/gym/523525/problem/B

from collections import defaultdict

size = int(input())
for i in range(size):
    n = int(input())
    val = list(map(int, input().split()))

    memo = defaultdict(int)

    def dp(num):
        if memo[num]:
            return memo[num]

        if num >= n:
            return 0

        ans = val[num] + dp(val[num]+num)

        memo[num] = ans
        return ans

    for i in range(n-1, -1, -1):
        dp(i)

    print(max(memo.values()))
