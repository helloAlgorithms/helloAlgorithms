class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
        q = deque()
        q.append((sr, sc))
        while q:
            x, y = q.popleft()
            if image[x][y] == color:
                continue
            image[x][y] = color
            for i in range(4):
                mx, my = x + dx[i], y + dy[i]
                if 0 <= mx < len(image) and 0 <= my < len(image[0]):
                    if image[mx][my] == start_color:
                        q.append((mx, my))
        return image
        