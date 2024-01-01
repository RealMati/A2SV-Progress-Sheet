class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3: return False
        

        slope=1
        for idx in range(1,len(arr)):
            if slope==1:
                if arr[idx]<=arr[idx-1]:
                    return False
                if idx+1<len(arr) and arr[idx]>arr[idx+1]:
                    slope=-1

            elif slope==-1:
                if arr[idx]>=arr[idx-1]:
                    return False
            

        if slope==-1: return True
        else: return False


        