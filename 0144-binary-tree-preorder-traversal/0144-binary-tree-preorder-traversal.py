# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        curr=root
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if not prev.right:
                    prev.right=curr
                    ans.append(curr.val)
                    curr=curr.left
                else:
                    prev.right=None
                    curr=curr.right
        return ans
        