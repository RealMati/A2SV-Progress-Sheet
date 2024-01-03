class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        p1=p2=0


        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                return nums1[p1]   
            elif nums1[p1]>nums2[p2]:
                p2+=1
            else:
                p1+=1
        return -1
        