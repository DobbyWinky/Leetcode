class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        adj=collections.defaultdict(list)
        for src,dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        freq=collections.defaultdict(int)

        def bfs(src, dest):
            queue=collections.deque([(src, [src])])
            vis=set()
            while queue:
                node, path=queue.popleft()
                if node==dest:
                    return path
                vis.add(node)
                for nei in adj[node]:
                    if nei not in vis:
                        queue.append((nei, path+[nei]))
        
        for src, dest in trips:
            path=bfs(src, dest)
            for p in path:
                freq[p]+=1
        
        memo=collections.defaultdict(int)

        def dp(node, parent, should_half):
            if (node, parent, should_half) in memo:
                return memo[(node, parent, should_half)]
            if should_half:
                cost=freq[node]*(price[node]//2)
            else:
                cost=freq[node]*price[node]
            
            for nei in adj[node]:
                if nei!=parent:
                    if should_half:
                        nei_cost=dp(nei, node, False)
                    else:
                        nei_cost=min(dp(nei, node, False),dp(nei, node, True))
                    
                    cost+=nei_cost
            memo[(node, parent, should_half)]=cost
            return cost
        cost=float('inf')
        for node in range(n):
            cost=min(cost, dp(node, None, True), dp(node, None, False))
        return cost
        
        