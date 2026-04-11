class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        rotten, time = 0,0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0,-1], [0,1],[1,0], [-1,0]]
        while len(q) > 0 and fresh >0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, cols = dr +r, dc +c
                    if (min(row,cols)<0 or row== ROWS or cols==COLS or grid[row][cols]!=1):
                        continue
                    #change to rotten
                    grid[row][cols] = 2
                    q.append([row,cols])
                    fresh -= 1
            #increse time
            time +=1
        return time if fresh==0 else -1         