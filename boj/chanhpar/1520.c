#include <stdio.h>

int m, n;
int map[500][500];
int dp[500][500];
char visit[500][500];

static const int dx[4] = {1, 0, -1, 0};
static const int dy[4] = {0, 1, 0, -1};

int
dfs(int row, int col) {
  int nx, ny;
  int i;

  if (visit[row][col]) {
    return dp[row][col];
  }

  if (row == m - 1 && col == n - 1) {
    visit[row][col] = 1;
    dp[row][col] = 1;
    return 1;
  }

  for (i = 0; i < 4; ++i) {
    nx = row + dx[i];
    ny = col + dy[i];
    if (nx < 0 || nx >= m || ny < 0 || ny >= n)
      continue;
    if (map[nx][ny] < map[row][col])
      dp[row][col] += dfs(nx, ny);
  }
  visit[row][col] = 1;
  return dp[row][col];
}

int
main(void) {
  int i, j;
  scanf("%d %d", &m, &n);
  for (i = 0; i < m; ++i)
    for (j = 0; j < n; ++j)
      scanf("%d", &map[i][j]);

  printf("%d\n", dfs(0, 0));
  return 0;
}
