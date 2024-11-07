# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size=mountain_arr.length()

        low,hi = 0,mountain_arr.length() - 1
        peak = None
        while low < hi:

            mid = (low + hi) // 2
            leftv = mountain_arr.get(mid - 1)
            rightv = mountain_arr.get(mid + 1)
            midv = mountain_arr.get(mid)
            
            if midv > rightv and midv > leftv:
                peak = mid
                break
            
            elif midv < rightv and midv > leftv:
                low = mid
            
            elif midv > rightv and midv < leftv:
                hi = mid 
        
        def bin_search(l, r, mode):
            while l<=r:
                mid=(l+r)//2
                
                if mountain_arr.get(mid)==target:
                    return mid
                
                if (mode=="incline" and target<mountain_arr.get(mid)) or (mode=="decline" and target>mountain_arr.get(mid)):
                    r=mid-1
                else:
                   l=mid+1

            return -1
        
        left=bin_search(0,peak, "incline")
        if left!=-1:
            return left
        right=bin_search(peak, size-1, "decline")
        if right!=-1:
            return right
        else:
            return -1

