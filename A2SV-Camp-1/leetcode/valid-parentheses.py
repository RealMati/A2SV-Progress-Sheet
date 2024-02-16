class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open={'{',"[","("}
        dic={"}":"{",']':'[',")":"("}

        for i in s:
            if i in open: stack.append(i)
            elif stack and stack[-1]==dic[i]:
                stack.pop()
            else:
                return False
            
        if stack:
                return False
        return True