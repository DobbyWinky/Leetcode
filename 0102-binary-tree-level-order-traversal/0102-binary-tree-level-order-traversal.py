# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        queue=[]
        queue.append(root)
        ans=[]
        while len(queue)>0:
            size=len(queue)
            curr=[]
            while size>0:
                pop=queue.pop(0)
                curr.append(pop.val)
                if pop.left!=None:
                    queue.append(pop.left)
                if pop.right!=None:
                    queue.append(pop.right)
                size-=1
            ans.append(curr)
        return ans
        