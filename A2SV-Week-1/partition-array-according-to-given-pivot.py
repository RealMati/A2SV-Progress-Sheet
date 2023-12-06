class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
            
        less=[]
        equal=[]
        greater=[]
        for num in nums:
            if num>pivot:
                greater+=[num]
            elif num<pivot:
                less+=[num]
            else:
                equal+=[num]
        return less+equal+greater