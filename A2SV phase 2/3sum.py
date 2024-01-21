class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sett=set()
        for i in range(len(nums)):
            target=nums[i]*-1
            l=i+1
            r=len(nums)-1

            while l<r:
                if l==i:
                    l+=1
                    continue
                elif r==i:
                    r-=1
                    continue 
                summ=nums[l]+nums[r]
                if summ==target:
                    sett.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1        
                elif summ<target:
                    l+=1
                else:
                    r-=1
        print(sett)
        return sett
            