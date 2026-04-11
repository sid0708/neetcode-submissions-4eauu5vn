# iterative bfs dont delete
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        island = 0
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r,c = q.popleft()
                for nr,nc in directions:
                    dr, dc = r+nr, c+nc
                    if min(dr,dc) <0 or dr >= ROWS or dc >= COLS or (dr,dc) in visit or grid[dr][dc] =="0":
                        continue
                    else:
                        q.append((dr,dc))
                        visit.add((dr,dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    island +=1
        return island