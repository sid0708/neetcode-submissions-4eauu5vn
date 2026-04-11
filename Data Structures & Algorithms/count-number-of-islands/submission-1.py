# iterative bfs dont delete
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        direction = [[-1,0],[1,0],[0,1],[0,-1]]
        
        visit = set()
        q = deque()
        def dfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                row,col = q.popleft()
                for dr, dc in direction:
                    nr, nc = dr + row, dc+col
                    if(min(nr,nc)<0 or nr==ROWS or nc==COLS or (nr,nc)in visit or grid[nr][nc] =="0"):
                        continue
                    visit.add((nr,nc))
                    q.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    island += 1
        return island
