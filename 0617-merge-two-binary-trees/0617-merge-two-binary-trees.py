# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1==None and root2==None:
                return None
            if root1==None and root2!=None:
                newNode = TreeNode(val=root2.val)
                newNode.left=dfs(None, root2.left)
                newNode.right=dfs(None, root2.right)
                return newNode
            if root1!=None and root2==None:
                newNode = TreeNode(val=root1.val)
                newNode.left=dfs(root1.left, None)
                newNode.right=dfs(root1.right, None)
                return newNode
            else:
                newNode = TreeNode(val=root1.val+root2.val)
                newNode.left=dfs(root1.left, root2.left)
                newNode.right=dfs(root1.right, root2.right)
                return newNode
        return dfs(root1, root2)
            
            
            
                
                
        