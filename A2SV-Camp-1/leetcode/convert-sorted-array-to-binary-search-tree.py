# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def c(left,right):
            if right-left:
                mid=(left+right)//2
                # print(left,right,mid)
                node=TreeNode(nums[mid])
                node.right=c(mid+1,right)
                node.left=c(left,mid) 
                return node
        return c(0,len(nums))

