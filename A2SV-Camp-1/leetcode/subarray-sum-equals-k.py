class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        summ=0
        ct=0

        for num in nums:
            summ+=num

            if summ-k in dic:
                ct+=dic[summ-k]
            if summ not in dic:
                dic[summ]=1
            else:
                dic[summ]+=1

        return ct