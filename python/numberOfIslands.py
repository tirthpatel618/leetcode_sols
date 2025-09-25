class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() 
        def dfs(i, j):
            if (
                i < 0 or j < 0 
                or i >= len(grid) or j >= len(grid[0]) 
                or (i, j) in visited 
                or grid[i][j] == '0'
            ):
                return
            visited.add((i, j))
            dfs(i+1, j) # down
            dfs(i-1, j) # up
            dfs(i, j+1) # right
            dfs(i, j-1) # left
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1
        return count