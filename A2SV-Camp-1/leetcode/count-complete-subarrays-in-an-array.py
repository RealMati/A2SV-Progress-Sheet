class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        goal=set(nums)
        count=0

        for l in range(len(nums)):
            cur=set()
            r=l

            while r<len(nums):
                cur.add(nums[r])

                if len(cur)==len(goal):
                    count+=1
                elif len(cur)>len(goal):
                    break

                r+=1

        return count