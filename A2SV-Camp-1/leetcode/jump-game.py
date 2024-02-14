class Solution:
    def canJump(self, nums: List[int]) -> bool:
        feasible_idx=len(nums)-1
        for idx in range(len(nums)-2,-1,-1):
                if nums[idx]+idx>=feasible_idx:
                    feasible_idx=idx
        return True if feasible_idx==0 else False
                

