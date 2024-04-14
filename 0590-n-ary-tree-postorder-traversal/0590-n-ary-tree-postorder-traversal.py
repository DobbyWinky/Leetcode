"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res=[]
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            self.res.append(root.val)
        dfs(root)
        return self.res
        
        