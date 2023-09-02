# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if root==None:
                return None
            leftTail=dfs(root.left)
            rightTail=dfs(root.right)
            if root.left:
                leftTail.right=root.right
                root.right=root.left
                root.left=None
            if rightTail:
                return rightTail
            if leftTail:
                return leftTail
            return root
        return dfs(root)
        