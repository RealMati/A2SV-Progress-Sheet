class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        ans=[]
        def c(a):
            if len(ans)==k: 
                res.append(ans[:])
                return 
            
            for i in range(a,n+1):
                ans.append(i)
                c(i+1)
                ans.pop()
        
        c(1)
        return res