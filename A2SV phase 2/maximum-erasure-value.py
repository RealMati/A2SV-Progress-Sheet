class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx=curSum=l=0
        dic=set()

        for r in range(len(nums)):
            if nums[r] not in dic:
                curSum+=nums[r]
                dic.add(nums[r])
            else:
                maxx=max(maxx,curSum)
                while nums[l]!=nums[r]:
                    curSum-=nums[l]
                    dic.remove(nums[l])
                    l+=1
                
                l+=1
        
        return max(maxx, curSum)

            
            
                
