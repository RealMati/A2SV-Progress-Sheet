class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        op={'+','-','/','*'}

        for ch in tokens:
            if ch not in op:
                stack.append(int(ch))
            else:
                if ch=='+':
                    ans=stack[-2]+stack[-1]
                elif ch=='-':
                    ans=stack[-2]-stack[-1]
                elif ch=='*':
                    ans=stack[-2]*stack[-1]
                else:
                    ans=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ans)
                # print(stack)

        return stack[-1]