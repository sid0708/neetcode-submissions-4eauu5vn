from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if grid[0][0]==1 or grid[-1][-1] ==1:
            return -1
        length = 1
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))
        directions = [[-1,0], [1,0],[0,-1], [0,1],(-1,-1), (-1,1), (1,-1), (1,1)]

        ROWS, COLS = len(grid), len(grid[0])
        while len(q) >0:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS-1 and c== COLS-1:
                    return length
                for dr, dc in directions:
                    nr, nc = dr +r, dc +c
                    if (min(nr,nc)<0 or nr>= ROWS or nc >= COLS or grid[nr][nc]==1 or (nr, nc)in visit):
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            length += 1
        return -1
            