# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        maxx=0

        def c(cur):
            nonlocal maxx
            if cur:
                dic[cur.val]+=1
                cur.left=c(cur.left)
                maxx=max(maxx, dic[cur.val])
                cur.right=c(cur.right)
                return cur
        c(root)
        ans=[]
        for key in dic:
            if dic[key]==maxx:
                ans.append(key)
        return ans