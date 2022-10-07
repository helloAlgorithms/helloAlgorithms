class Solution:
    def bfs(self, i, j, grid, m, n):
        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
        q = deque()
        q.append((i, j))
        grid[i][j] = "0"
        while q:
            x, y = q.popleft()
            for k in range(4):
                mx, my = x + dx[k], y + dy[k]
                if 0 <= mx < m and 0 <= my < n and grid[mx][my] == "1":
                    grid[mx][my] = "0"
                    q.append((mx, my))
        return 1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += self.bfs(i, j, grid, m, n)
        return island
        