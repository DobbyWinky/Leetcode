# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        queue.append([root, 0,0])
        order=collections.defaultdict(lambda:collections.defaultdict(list))
        while len(queue)>0:
            size=len(queue)
            while size>0:
                node, col, row=queue.pop(0)
                order[col][row].append(node.val)
                order[col][row].sort()
                if node.left!=None:
                    queue.append([node.left, col-1,row+1])
                if node.right!=None:
                    queue.append([node.right, col+1, row+1])
                size-=1
        ans=[]
        for k in sorted(order):
            curr=[]
            for v in order[k].items():
                for x in v[1]:
                    curr.append(x)
            ans.append(curr)
                
        return ans
        