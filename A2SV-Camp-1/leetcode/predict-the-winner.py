class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dic = {}
        
        def c(i,j):
            if (i,j) in dic:
                return dic[i,j]
            if i>j:
                return 0
            
            p1 = nums[i] + min( c(i+1,j-1), c(i+2,j  ) ) 
            p2 = nums[j] + min( c(i  ,j-2), c(i+1,j-1) )

            res = max(p1,p2)
            dic[i,j] = res
            return res

        ans=c(0,len(nums)-1)
        return ans >= sum(nums)-ans

            
