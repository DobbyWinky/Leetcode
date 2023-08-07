# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1=[]
        path2=[]
        def path(root,paths, node):
            if root==None:
                return False
            paths.append(root)
            if root==node:
                return True
            if path(root.left, paths, node) or path(root.right,paths, node):
                return True
            paths.pop()
            
        path(root,path1,p)
        path(root,path2,q)
        for i in range(min(len(path1), len(path2))):
            if path1[i]!=path2[i]:
                return path1[i-1]
        if i==len(path1)-1:
            return path1[i]
        if i==len(path2)-1:
            return path2[i]
        print("hello")
        return None
        