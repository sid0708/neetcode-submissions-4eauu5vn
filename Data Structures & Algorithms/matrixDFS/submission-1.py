class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, seen):
            ROWS, COLS = len(grid), len(grid[0])
            # base condiions
            if min(r,c) <0 or r == ROWS or c == COLS or (r,c) in seen or grid[r][c] ==1:
                return 0
            if r == ROWS -1 and c== COLS-1:
                return 1
            seen.add((r,c))
            count =0
            # traverse from first matrix ele
            count += dfs(grid, r-1, c, seen)
            count += dfs(grid, r+1, c, seen)
            count += dfs(grid, r, c-1, seen)
            count += dfs(grid, r, c+1, seen)
            seen.remove((r,c))
            return count
        return dfs(grid, 0,0, set())

        