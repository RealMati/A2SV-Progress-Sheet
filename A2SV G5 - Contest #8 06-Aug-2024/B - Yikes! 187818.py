# Problem: B - Yikes! - https://codeforces.com/gym/511242/problem/B

size = int(input())
nums = list(map(int, input().split()))
k = int(input())
q = list(map(int, input().split()))

rangee=[]

start=0
for num in nums:
    rangee.append([start+1, num+start])
    start=num+start

# print(rangee)
sortt=sorted(q)
res={}

idx=0
for i in range(size):
    start, end = rangee[i]
    while idx<len(sortt) and start<=sortt[idx]<=end:
        res[sortt[idx]]=i+1
        # print(sortt[idx], i+1)
        idx+=1

for num in q:
    print(res[num])
    

