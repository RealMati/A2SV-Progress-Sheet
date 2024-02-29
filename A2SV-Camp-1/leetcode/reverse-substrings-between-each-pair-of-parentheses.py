class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i]==')':
                ch=""
                while stack[-1]!='(':
                    ch=stack[-1]+ch
                    stack.pop()
                stack.pop()
                stack.append(ch[::-1])

            else: stack.append(s[i])
                        

        return "".join(stack)