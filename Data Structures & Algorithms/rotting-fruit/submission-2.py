class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        while len(q)>0  and fresh >0:
            for _ in range(len(q)) :
                r, c = q.popleft()
                for nr, nc in directions:
                    dr, dc = r+nr, c+nc
                    if (min(dr,dc) <0 or dr>= ROWS or  dc >=COLS or grid[dr][dc]!=1):
                        continue
                    else:
                        grid[dr][dc] =2
                        q.append((dr, dc))
                        fresh -=1
            time += 1
        return time if fresh == 0 else -1

