# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[]
        queue.append([root,0])
        ans=1
        while len(queue)>0:
            size=len(queue)
            minVal=queue[0][1]
            
            first=0
            last=0
            for i in range(size):
                pop=queue.pop(0)
                node=pop[0]
                index=pop[1]
                if node.left!=None:
                    queue.append([node.left, 2*(index-minVal)+1])
                if node.right!=None:
                    queue.append([node.right,2*(index-minVal)+2])
                if i==0:
                    first=index
                if i==size-1:
                    last=index
            ans=max(ans, last-first+1)
        return ans
                