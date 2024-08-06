# Problem: A - Large Number - https://codeforces.com/gym/511242/problem/A

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    nums=input()

    pos=n
    for i in range(n):
        if nums[i]<str(k):
            pos=i
            break

    print(nums[:pos]+str(k)+nums[pos:])