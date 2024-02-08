class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}
        ct=0
        prefix=0

        
        for num in nums:
            prefix+=num

            if prefix%k in dic:
                ct+=dic[prefix%k]
                dic[prefix%k]+=1
            else:
                dic[prefix%k]=1

        return ct