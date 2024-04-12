# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def forward(c,idx):
            cur=list(c)
            res=int(cur[idx])
            if res!=9:
                res+=1
            else:
                res=0
            cur[idx]=str(res)
            return cur

        def backward(c,idx):
            cur=list(c)
            res=int(cur[idx])
            if res!=0:
                res-=1
            else:
                res=9
            cur[idx]=str(res)
            return cur
        # return 0
        deads=set(deadends)
        q=deque()
        q.append(['0','0','0','0'])
        visited=set()
        visited.add(('0','0','0','0'))
        level=-1
        if "0000" in deads: return -1

        while q:
            level+=1

            for i in range(len(q)):
                cur=q.popleft()
                s="".join(cur)
                if s==target:
                    return level

                for i in range(4):
                    new=forward(cur,i)
                    strnew="".join(new)
                    new2=backward(cur,i)
                    strnew2="".join(new2)


                    if tuple(new) not in visited and strnew not in deads:
                        q.append(new)
                        visited.add(tuple(new))
                    if tuple(new2) not in visited and strnew2 not in deads:
                        q.append(new2)
                        visited.add(tuple(new2))

        return -1


