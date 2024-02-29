# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def divide(left,right):
            if right-left==1: return left
            elif right==left: return 
            mid=math.ceil((left+right)/2)

            l=divide(left,mid) 
            r=divide(mid,right)
            if nums[l]>nums[r]:
                return l
            else: return r

        def conquer(left,right):
            maxx=divide(left,right)
            if maxx!=None:
                node=TreeNode(nums[maxx])
                node.right=conquer(maxx+1,right)
                node.left=conquer(left,maxx)
                return node

        return conquer(0,len(nums))