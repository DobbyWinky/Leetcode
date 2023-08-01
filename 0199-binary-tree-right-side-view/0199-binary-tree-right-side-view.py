# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        queue=[]
        ans=[]
        queue.append(root)
        while len(queue)>0:
            size=len(queue)
            while size>0:
                if size==1:
                    ans.append(queue[0].val)
                pop=queue.pop(0)
                if pop.left!=None:
                    queue.append(pop.left)
                if pop.right!=None:
                    queue.append(pop.right)
                size-=1
        return ans
        