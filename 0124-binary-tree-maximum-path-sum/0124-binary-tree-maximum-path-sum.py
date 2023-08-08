# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        def dfs(root):
            if root==None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            self.ans=max(self.ans, root.val, left+root.val, right+root.val, left+right+root.val)
            return root.val + max(0,left,right)
        dfs(root)
        return self.ans
        