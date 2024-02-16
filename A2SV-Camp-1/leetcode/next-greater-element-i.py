class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dic={}

        for num in nums2:
            if not stack: stack.append(num)
            elif num>stack[-1]:
                while stack and num>stack[-1]:
                    dic[stack[-1]]=num
                    stack.pop()
            else:
                dic[stack[-1]]=-1
            stack.append(num)

        res=[]
        for num in nums1:
            res.append(dic.get(num,-1))
        # print(dic)
        return res
