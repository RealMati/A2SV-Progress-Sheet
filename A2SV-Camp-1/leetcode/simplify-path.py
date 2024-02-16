class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        stack=[]
        for i in a:
            if i=='.': continue
            elif i=="..": 
                if stack: stack.pop()
            elif i:
                stack.append(i)
        # print(stack)
        return "/"+"/".join(stack)
