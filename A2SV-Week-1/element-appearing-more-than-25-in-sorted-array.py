class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count=Counter(arr)

        for key in count:
            if count[key]>len(arr)/4:
                return key