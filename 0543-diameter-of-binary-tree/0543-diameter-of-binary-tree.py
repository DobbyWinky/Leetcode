# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
ans=0
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(root):
            if root==None:
                return 0
            left=diameter(root.left)
            right=diameter(root.right)
            if left+right>self.dia:
                self.dia=left+right
            return 1+max(left, right)
        self.dia=0
        diameter(root)
        return self.dia
        