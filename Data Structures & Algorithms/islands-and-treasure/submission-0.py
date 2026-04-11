from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(-1,0), (1, 0), (0,1), (0,-1)]

        def bfs(r,c):
            q = deque()
            seen =set()
            steps = 0
            q.append((r,c))
            seen.add((r,c))
            while len(q)>0:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0: 
                        return steps
                    for nr, nc in directions:
                        # al conditions not met
                        dr, dc = nr+r, nc+c
                        if(min(dr,dc)< 0 or dr>= ROWS or dc>=COLS or (dr,dc) in seen or grid[dr][dc]==-1):
                            continue
                        else:
                            q.append((dr,dc))
                            seen.add((dr,dc))
                steps += 1
            return INF
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
