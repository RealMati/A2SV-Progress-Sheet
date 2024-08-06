# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

    size=int(input())
    nums=list(map(int, input().split()))
     
    res=0
    l=0
    r=1
    maxx=nums[l]
    while l<r and r<size:
        if maxx<nums[r]:
            maxx=nums[r]
            if r==size-1:
                res=max(res, r-l+1)
            r+=1
        else:
            maxx=nums[r]
            res=max(res, r-l)
            l=r
            r+=1
    print(res if res else size)
     