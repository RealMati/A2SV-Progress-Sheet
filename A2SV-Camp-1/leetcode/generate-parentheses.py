class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        ans=[]
        opt=['(',')']

        def c(open,close):
            if open==n and close==n:
                res.append("".join(ans))
                return 
            
            for o in opt:
                if open==n and o=='(': continue
                elif close==n and o==')': continue
                if open==0 and o==")": continue
                if open==close and o==')': continue
                ans.append(o)
                if o=='(': c(open+1,close)
                else: c(open,close+1)
                ans.pop()

            return res
        return c(0,0)
        