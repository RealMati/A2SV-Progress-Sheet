# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dic=defaultdict(list)
        root.val=1
        def c(cur,level):

            if cur:
                dic[level].append(cur.val)
                if cur.left: 
                    cur.left.val=cur.val*2
                    c(cur.left,level+1)
                if cur.right: 
                    cur.right.val=cur.val*2 +1
                    c(cur.right,level+1)

        c(root,0)
        # print(dic)
        maxx=0
        for arr in dic.values():
            maxx=max(maxx, arr[-1]-arr[0])

        return maxx+1