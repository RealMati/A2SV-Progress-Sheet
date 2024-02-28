class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        nums=[]
        res=[]
        for i in range(len(s)):
            if s[i]==']':
                idx=i
                ch=""
                while stack[-1]!='[':
                    ch=stack[-1]+ch
                    stack.pop()
                stack.pop()
                num=""
                while stack and len(stack[-1])==1 and 48<=ord(stack[-1])<=57:
                    num= stack[-1]+num
                    stack.pop()
                ch=ch*int(num)
                stack.append(ch)

            else: stack.append(s[i])
                        

        return "".join(stack)