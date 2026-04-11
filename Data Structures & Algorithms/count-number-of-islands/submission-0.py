# iterative bfs dont delete
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == "0" or (nr, nc) in visit
                    ):
                        continue
                    visit.add((nr, nc))
                    q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
