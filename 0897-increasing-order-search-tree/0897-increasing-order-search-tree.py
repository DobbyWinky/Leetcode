# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node=TreeNode(0)
        self.dummy=node
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.dummy.right=TreeNode(root.val)
            self.dummy=self.dummy.right
            dfs(root.right)
            return
        dfs(root)
        return node.right
            
        
        