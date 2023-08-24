# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res=[]
        def dfs(root):
            if root==None:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        self.i=0
        res=data.split(",")
        def dfs():
            if res[self.i]=="N":
                return None
            newNode=TreeNode(int(res[self.i]))
            self.i+=1
            newNode.left=dfs()
            self.i+=1
            newNode.right=dfs()
            return newNode
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))