# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

size = int(input())
for i in range(size):
    num = int(input())
    ans=0
    zero=one=None
    length=ct=0
    for i in range(32):
        if num&1<<i: 
            length=i+1
            ct+=1

    
    for i in range(length):
        if num&1<<i:
            one=i
            break
    for i in range(length):
        if num&1<<i==0:
            zero=i
            break
    ans |= 1<<one
    if ct==1:
        if zero!=None:
            ans|=1<<zero
        else:
            ans|=1<<length

    print(ans)


    
    
    
