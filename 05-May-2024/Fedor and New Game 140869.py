# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = list(map(int, input().split()))
nums=[]
for i in range(m):
    num = int(input())
    nums.append(num)
    # print(bin(num))

check = int(input())
res=0
for num in nums:
    diff=0
    for i in range(21):
        if num&1<<i!=check&1<<i:
            diff+=1
    if diff<=k:
        res+=1
print(res)

