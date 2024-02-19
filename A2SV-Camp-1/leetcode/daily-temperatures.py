class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for idx,num in enumerate(temperatures):
            while stack and num>temperatures[stack[-1]]:
                res[stack[-1]] = idx-stack[-1]
                stack.pop()
            stack.append(idx)
        
        return res