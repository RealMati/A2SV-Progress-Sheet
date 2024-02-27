class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        res=set()
        arr=[]
        summ=0
        def c(idx):
            nonlocal summ
            if summ==target:
                res.add(tuple(sorted(arr[:])))
                return
            if summ>target: return 

            for i in range(idx-1,len(cand)):
                arr.append(cand[i])
                summ+=cand[i]
                c(i+1)
                arr.pop()
                summ-=cand[i]
        c(0)
        return res
