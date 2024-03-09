class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res=[]
        for idx,num in enumerate(index):
            res.insert(num, nums[idx])
            # print(res)
        return res
