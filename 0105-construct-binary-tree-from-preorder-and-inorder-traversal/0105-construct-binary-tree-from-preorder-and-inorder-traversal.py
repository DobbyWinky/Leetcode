# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        newNode=TreeNode(preorder[0],None, None)
        i=0
        for i in range(len(inorder)):
            if preorder[0]==inorder[i]:
                break 
        newNode.left=self.buildTree(preorder[1:i+1], inorder[:i])
        newNode.right=self.buildTree(preorder[i+1:], inorder[i+1:])
        return newNode
        
        
        
        
            
        