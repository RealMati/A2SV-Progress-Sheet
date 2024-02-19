class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = [nums2[0]]
        for num in nums2:
            while stack and stack[-1]<num:
                mp[stack[-1]] = num
                stack.pop()
            stack.append(num)
        while stack:
            mp[stack[-1]] = -1
            stack.pop()
        arr = []
        for num in nums1:
            arr.append(mp[num])
        return arr
