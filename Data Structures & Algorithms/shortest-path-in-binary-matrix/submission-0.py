from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,-1),(0,1),(1,0),(-1,0),
                      (1,-1),(1,1),(-1,1),(-1,-1)]

        q = deque([(0, 0, 1)])
        visit = {(0, 0)}

        while q:
            r, c, length = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                    grid[nr][nc] == 1 or (nr, nc) in visit
                ):
                    continue
                visit.add((nr, nc))
                q.append((nr, nc, length + 1))

        return -1