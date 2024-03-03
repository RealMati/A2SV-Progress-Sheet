class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        dic={}

        for idx,num in enumerate(nums):
            if (idx+num) % len(nums) in dic:
                cur=(idx+nums[idx])%len(nums)
                while cur in dic and dic[cur]!=idx:
                    cur=dic[cur]
                    
                if cur!=None and cur in dic and dic[cur]==idx: return True
            
            if (idx+num) % len(nums) in dic and dic[(idx+num) % len(nums)]==None: dic[idx]=None
            elif nums[(idx+num) % len(nums)] * num <0: dic[idx]=None
            else:
                if idx!=(idx+num) % len(nums):
                    dic[idx]=(idx+num) % len(nums)
                else: dic[idx]=None
            
        return False

       