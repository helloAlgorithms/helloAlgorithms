#include <stdio.h>

char board[100][100];
int m, n;

int
cmp(const void* a, const void* b) {
  return *(const int*)a > *(const int*)b ? 1 : -1;
}

int
dfs(int row, int col) {
  static const int dx[] = {1, 0, -1, 0};
  static const int dy[] = {0, 1, 0, -1};
  int i;
  int count, nx, ny;

  count = 1;
  board[row][col] = 1;
  for (i = 0; i < 4; ++i) {
    nx = row + dx[i];
    ny = col + dy[i];
    if (nx < 0 || nx >= m || ny < 0 || ny >= n || board[nx][ny] == 1)
      continue;
    count += dfs(nx, ny);
  }
  return count;
}

int
main(void) {
  int k, x1, y1, x2, y2;
  int i, j;
  int areas[10000];
  int count;
  scanf("%d %d %d", &m, &n, &k);
  while (k--) {
    scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
    for (i = x1; i < x2; ++i)
      for (j = y1; j < y2; ++j)
        board[i][j] = 1;
  }

  count = 0;
  for (i = 0; i < m; ++i)
    for (j = 0; j < n; ++j)
      if (board[i][j] == 0)
        areas[count++] = dfs(i, j);

  qsort(areas, count, sizeof(int), cmp);

  printf("%d\n", count);
  for (i = 0; i < count; ++i)
    printf("%d ", areas[i]);
  return 0;
}
