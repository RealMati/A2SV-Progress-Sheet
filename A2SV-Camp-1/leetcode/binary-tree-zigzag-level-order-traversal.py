# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        res[0].append(root.val)

        def c(cur, level):
            if cur:
                ans = []
                left = []
                right = []
                if cur.left:
                    ans.append(cur.left.val)
                if cur.right:
                    ans.append(cur.right.val)

                if ans:
                    res[level].extend(ans)

                cur.left = c(cur.left, level + 1)
                cur.right = c(cur.right, level + 1)
                return cur

        c(root, 1)
        for key in res:
            if key%2: res[key]=res[key][::-1]
        return res.values()
