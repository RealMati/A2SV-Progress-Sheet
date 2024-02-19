class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        a=[[-1,len(arr)] for _ in range(len(arr))]
        res=0

        for idx,num in enumerate(arr):
            if not stack: stack.append(idx)
            else:
                while stack and arr[stack[-1]]>=num:
                    a[stack[-1]][1]=idx
                    stack.pop()
                stack.append(idx)
        # print(nextdic)
        stack=[]
        for idx in range(len(arr)-1,-1,-1):
            if not stack: stack.append(idx)
            while stack and arr[stack[-1]]>arr[idx]:
                a[stack[-1]][0]=idx
                stack.pop()
            stack.append(idx)
        # print(beforedic)
        # print(a)
        for i in range(len(arr)):
            right=a[i][1]-i
            left=i-a[i][0]
            
            # print((left*right)*arr[i],arr[i],[left,beforedic[i],i],right)
            res += (left*right)*arr[i]

        return res % (10**9 + 7)
        # return 