class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj=collections.defaultdict(list)
        for road in roads:
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
        ans=0
        for i in range(n):
            for j in range(i+1, n):
                value=len(adj[i])+len(adj[j])
                if [i,j] in roads or [j,i] in roads:
                    value-=1
                ans=max(ans, value)
         
        return ans
        