class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        minisum = 0
        presum = [0]*len(arr) 
        suffix = [len(arr)]*len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                suffix[stack.pop()] = i  
            if not stack:
                presum[i] = (i+1)
            else:
                presum[i]= (i-stack[-1])
            stack.append(i)
        for i in range(len(arr)):
            minisum += (presum[i])*(suffix[i]-i)*arr[i]
        return minisum%(10**9 + 7)