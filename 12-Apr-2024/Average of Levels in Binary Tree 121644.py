# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append((root,0))
        check=[]
        dic=defaultdict(lambda: [0,0])
        
        while q:
            cur,level=q.popleft()
            dic[level]=[(dic[level][0]+cur.val),dic[level][1]+1]

            if cur.left:
                q.append((cur.left, level+1))
            if cur.right:
                q.append((cur.right, level+1))
        
        for key in dic:
            dic[key]=dic[key][0]/dic[key][1]
        return dic.values()