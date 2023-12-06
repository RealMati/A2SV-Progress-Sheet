class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        positive_list=[i for i in nums if i>0]
        negative_list=[i for i in nums if i<0]
        for i in range(len(positive_list)):
            res.append(positive_list[i])
            res.append(negative_list[i])
            
        return res