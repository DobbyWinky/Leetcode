class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)
        for p in paths:
            adj[p[0]].append(p[1])
            adj[p[1]].append(p[0])
        color=[0]*(n+1)
        ans=[]
        def possibleToColor(node, col, color):
            for nei in adj[node]:
                if color[nei]==col:
                    return False
            return True
        def helper(node):
            if node==n+1:
                return True
            for col in range(1,5):
                if possibleToColor(node,col, color):
                    color[node]=col
                    if helper(node+1):
                        return True
                    color[node]=0
            return False
        helper(1)
        ans=[]
        for c in color:
            if c!=0:
                ans.append(c)
        return ans