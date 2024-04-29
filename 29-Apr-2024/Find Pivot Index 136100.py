# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_summ=[0]
        for i in nums:
            prefix_summ.append(i+prefix_summ[-1])
        res=-1
        for j in range(1,len(prefix_summ)):
            if prefix_summ[-1]-prefix_summ[j]==prefix_summ[j-1]:
                return j-1
        return -1

