# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res=[]
        def c(cur,v,ans):
            if cur:
                ans.append(cur)
                if cur.val==v.val: 
                    res.append(ans)
                if cur.val<v.val:
                    c(cur.right,v,ans)
                elif cur.val>v.val:
                    c(cur.left,v,ans)
                return res[-1]
            
        pres=c(root,p,[])
        qres=c(root,q,[])
        for i in range(min(len(qres),len(pres))):
            if pres[i] is qres[i]:
                last=pres[i]
            else: break
        return last
       