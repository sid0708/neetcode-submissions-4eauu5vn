from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Use set instead of list for visited nodes
        visited = set()
        
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        components = 0
        
        # Check every node (0 to n-1)
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components += 1
                
        return components