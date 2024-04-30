# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n,q= list(map(int, input().split()))
parent={i:i for i in range(1,n+1)}
rank={i:0 for i in range(1,n+1)}  
minn={i:i for i in range(1,n+1)}  
maxx={i:i for i in range(1,n+1)} 
carry={i:1 for i in range(1,n+1)}  
 

def find(x):
    cur = x
    while cur != parent[cur]:
        cur = parent[cur]

    cur1=x
    while cur1!=parent[cur1]:
        parent[cur1]=cur
        cur1=parent[cur1]
    
    return cur

def union(a, b):
    parentA = find(a)
    parentB = find(b)
    rankA=rank[parentA]
    rankB=rank[parentB]

    if parentA!=parentB:
        if rankA>rankB:
            parent[parentB] = parentA
            carry[parentA]+=(carry[parentB])
            minn[parentA]=min(minn[parentA], minn[parentB])
            maxx[parentA]=max(maxx[parentA], maxx[parentB])

        elif rankA<rankB:
            parent[parentA] = parentB
            carry[parentB]+=(carry[parentA])
            minn[parentB]=min(minn[parentA], minn[parentB])
            maxx[parentB]=max(maxx[parentA], maxx[parentB])

        else:
            parent[parentA] = parentB
            carry[parentB]+=(carry[parentA])
            minn[parentB]=min(minn[parentA], minn[parentB])
            maxx[parentB]=max(maxx[parentA], maxx[parentB])
            rank[parentB]+=1            
                

for i in range(q):
    query=input().split()
    if query[0]=="union":
        union(int(query[1]), int(query[2]))
    else:
        par=find(int(query[1]))
        print(minn[par], maxx[par], carry[par])