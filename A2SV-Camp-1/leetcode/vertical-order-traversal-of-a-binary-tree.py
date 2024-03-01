# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        def c(cur, row, col):
            if cur:
                dic[col].append([row, cur.val])
                c(cur.left, row + 1, col - 1)
                c(cur.right, row + 1, col + 1)

        c(root, 0, 0)

        for key in dic:
            dic[key].sort()
            for i in range(len(dic[key])):
                dic[key][i] = dic[key][i][1]

        dic = sorted(dic.items())

        for i in range(len(dic)):
            dic[i] = dic[i][1]
            
        return dic
