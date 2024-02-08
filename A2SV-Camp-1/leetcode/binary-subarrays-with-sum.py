class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        ct=prefix=0

        for num in nums:
            prefix+=num

            if prefix-goal in dic:
                ct+=dic[prefix-goal]

            dic[prefix]+=1

        return ct