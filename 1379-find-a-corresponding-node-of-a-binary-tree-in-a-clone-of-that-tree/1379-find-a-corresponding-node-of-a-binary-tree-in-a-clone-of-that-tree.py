# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans=None
        def dfs(root1, root2):
            if root1==None:
                return
            if root1==target:
                self.ans=root2
                return
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)
        dfs(original, cloned)
        return self.ans
                
        
        