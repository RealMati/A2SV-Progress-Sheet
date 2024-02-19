class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        stack=[]
        dic={}

        for idx,num in enumerate(temperatures):
            while stack and num>temperatures[stack[-1]]:
                dic[stack[-1]] = idx-stack[-1]
                stack.pop()
            stack.append(idx)
        
        for i in range(len(temperatures)):
            res.append(dic.get(i,0))
        return res