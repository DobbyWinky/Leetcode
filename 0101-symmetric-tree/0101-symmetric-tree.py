# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSameTree(self,tree1, tree2):
        if tree1==None and tree2==None:
            return True
        if tree1==None:
            return False
        if tree2==None:
            return False
        return tree1.val==tree2.val and self.checkSameTree(tree1.left, tree2.right) and self.checkSameTree(tree1.right, tree2.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.checkSameTree(root.left, root.right)
        