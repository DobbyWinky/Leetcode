# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths=[]
        def traversal(root, curr):
            curr+=str(root.val)
            if root.left==None and root.right==None:
                paths.append(curr)
                return
            if root.left!=None:
                traversal(root.left, curr+"->")
            if root.right!=None:
                traversal(root.right, curr+"->")
            return
        
        if root==None:
            return []
        traversal(root, "")
        return paths
        
        