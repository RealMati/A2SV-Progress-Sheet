# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

num = int(input())

ct=0
for i in range(32):
    if num&1<<i: 
        ct+=1
print(ct)



    
    
    
