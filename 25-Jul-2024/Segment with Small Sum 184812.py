# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

length, s=list(map(int, input().split()))
nums=list(map(int, input().split()))

l=0
r=1
summ=nums[0]
maxx=0

while r<=length:
    if summ<=s:
        if r<length: summ+=nums[r]
        r+=1
    else:
        maxx=max(maxx, r-l-1)
        summ-=nums[l]
        l+=1
if summ<=s:
    maxx=max(maxx, r-l-1)
print(maxx)