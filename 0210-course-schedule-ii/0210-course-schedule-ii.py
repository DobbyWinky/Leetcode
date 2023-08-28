class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        vis=collections.defaultdict(int)
        ans=[]
        def dfs(course):
            if vis[course]==2:
                return True
            vis[course]=2
            for nei in adj[course]:
                if vis[nei]!=1 and dfs(nei):
                    return True
            vis[course]=1
            ans.append(course)
        for n in range(numCourses):
            if vis[n]!=1 and dfs(n):
                return []
        return ans
        
        