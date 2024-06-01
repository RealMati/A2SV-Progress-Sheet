# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        
        def delete(cur,key):
            #getting the node to be deleted
            if cur:
                if cur.val>key:
                    cur.left=delete(cur.left,key)
                    return cur
                elif cur.val<key:
                    cur.right=delete(cur.right,key)
                    return cur
                else:
                    #IF LEAFNODE
                    if not cur.left and not cur.right:
                        return None
                    # if one child
                    if cur.left and not cur.right:
                        return cur.left
                    elif not cur.left and cur.right:
                        return cur.right
                    #if two child
                    else:
                        node=cur
                        cur=cur.right
                        while cur.left:
                            cur=cur.left
                        node.val=cur.val
                        node.right=delete(node.right,node.val)
                        return node
            else:
                return cur

        return delete(root,key)
                    

