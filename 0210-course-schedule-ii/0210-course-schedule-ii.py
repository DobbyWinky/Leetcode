class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=collections.defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        vis=collections.defaultdict(int)
        ans=[]
        def cycle(course):
            if vis[course]==2:
                return True
            vis[course]=2
            for nei in adj[course]:
                if vis[nei]!=1 and cycle(nei):
                    return True
            vis[course]=1
            ans.append(course)
            return False
        for i in range(numCourses):
            if vis[i]!=1 and cycle(i):
                return []
        return ans
        
        