class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        count=Counter(nums)
        res=[]
        for num in count:
            if count[num]>(len(nums)/3):
                res.append(num)
        return res
        