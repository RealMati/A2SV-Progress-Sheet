class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[-1]*(len(nums1)+1)
        sett={}
        for idx,num in enumerate(nums1):
            sett[num]=idx

        for num in nums2:
            while stack and stack[-1][1]<num:
                res[stack[-1][0]]=num
                stack.pop()
            if num in sett: stack.append([sett[num],num])
            else: stack.append([len(nums1),num])
        
        res.pop()
        return res