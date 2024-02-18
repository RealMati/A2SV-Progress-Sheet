class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        res=0

        for i in range(len(s)):
            if s[i]=='(': stack.append(s[i])
            else:
                if s[i-1]=='(':
                    res += 2**(len(stack)-1)
                stack.pop()

        return res
                     