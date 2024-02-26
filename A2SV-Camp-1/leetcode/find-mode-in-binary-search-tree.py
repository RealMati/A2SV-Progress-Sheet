# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def c(cur):
            if cur:
                dic[cur.val]+=1
                cur.left=c(cur.left)
                cur.right=c(cur.right)
                return cur
        c(root)
        ans=[]
        v=max(dic.values())
        for key in dic:
            if dic[key]==v:
                ans.append(key)
        return ans