class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCt=0
        product=1
        res=[]
        
        for num in nums:
            if num:
                product*=num
            else:
                zeroCt+=1
        
        for num in nums:
            if zeroCt==0 and num:
                res.append(product//num)
            elif zeroCt>0 and num:
                res.append(0)
            elif zeroCt>1 and num==0:
                res.append(0)
            elif zeroCt==1 and num==0:
                res.append(product)
        
        return res