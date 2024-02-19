class Solution(object):
    def isValid(self, s):
        stack = []
        map = {"}":"{",")":"(","]":"["}
        for par in s:
            if par in map:
                if len(stack)!= 0 and stack[-1] == map[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return True if len(stack) == 0 else False