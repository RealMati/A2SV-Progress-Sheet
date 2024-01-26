class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=zeroCt=maxx=0

        for r in range(len(nums)):
            if nums[r]:
                continue

            zeroCt+=1

            if zeroCt>k:
                maxx=max(maxx,r-l)
                while zeroCt>k:
                    if nums[l]:
                        l+=1
                    else:
                        zeroCt -= 1
                        l+=1
                       
        maxx=max(maxx, len(nums)-l)

        return maxx