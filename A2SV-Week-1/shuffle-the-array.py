class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[0]*len(nums)
        space=0
        for i in range(n):
            res[space]=nums[i]
            res[(n*2-1)-space]=nums[(n*2-1)-i]
            space+=2
        return res
