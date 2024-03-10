class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i]=="D":
                stack.append(stack[-1]*2)
            elif operations[i]=="C":
                stack.pop(-1)
            elif operations[i]=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operations[i]))
        # print(stack)
        return sum(stack)

