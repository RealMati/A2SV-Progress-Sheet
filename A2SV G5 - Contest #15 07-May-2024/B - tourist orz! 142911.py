# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

size = int(input())
for i in range(size):
    n, k = list(map(int, input().split()))
    nums= list(map(int, input().split()))

    maxx=0
    for num in nums:
        maxx=max(maxx, num|k)
    print(maxx)