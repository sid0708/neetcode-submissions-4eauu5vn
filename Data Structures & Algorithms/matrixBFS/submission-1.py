from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        q = deque()
        q.append((0,0))
        seen.add((0,0))
        length = 0
        while len(q):
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS -1 and c == COLS -1:
                    return length
                for dr, dc in directions:
                    nr, nc = r+dr, c +dc
                    if (min(nr,nc) <0 or nr>= ROWS or nc >= COLS or (nr,nc)in seen or grid[nr][nc]==1):
                        continue
                    else:
                        q.append((nr,nc))
                        seen.add((nr,nc))
            length += 1
        return -1


            
                